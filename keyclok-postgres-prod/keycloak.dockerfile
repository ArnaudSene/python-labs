FROM quay.io/keycloak/keycloak-x:latest as builder

ENV KC_METRICS_ENABLED=true
ENV KC_FEATURES=token-exchange
ENV KC_DB=postgres
RUN /opt/keycloak/bin/kc.sh build

FROM quay.io/keycloak/keycloak-x:latest
COPY --from=builder /opt/keycloak/lib/quarkus/ /opt/keycloak/lib/quarkus/
WORKDIR /opt/keycloak
  # for demonstration purposes only, please make sure to use proper certificates in production instead
#RUN keytool -genkeypair -storepass password -storetype PKCS12 -keyalg RSA -keysize 2048 -dname "CN=server" -alias server -ext "SAN:c=DNS:localhost,IP:127.0.0.1" -keystore conf/server.keystore
ENV DOMAIN_SUBDOMAIN=pyapps.site
ENV KEYCLOAK_SSL_ALIAS=keycloak_ssl
ENV KEYCLOAK_SSL_PASSWORD=keycloak_ssl_password
ENV KEYSTORE_PASSWORD=keycloak_keystore_password

RUN openssl pkcs12 -export -in /etc/letsencrypt/live/DOMAIN_SUBDOMAIN/fullchain.pem -inkey /etc/letsencrypt/live/DOMAIN_SUBDOMAIN/privkey.pem -out /etc/letsencrypt/live/DOMAIN_SUBDOMAIN/pkcs.p12 -name KEYCLOAK_SSL_ALIAS -passout pass:KEYCLOAK_SSL_PASSWORD

RUN cd /opt/keycloak/current/standalone/configuration

RUN keytool -keystore keycloak.jks -genkey -alias key_to_be_deleted

ENV KEYCLOAK_ADMIN=admin
ENV KEYCLOAK_ADMIN_PASSWORD=password
  # change these values to point to a running postgres instance
ENV KC_DB_URL=db
ENV KC_DB_USERNAME=docker
ENV KC_DB_PASSWORD=password
ENV KC_HOSTNAME=localhost:8443
ENTRYPOINT ["/opt/keycloak/bin/kc.sh", "start", "--https-certificate-file=/etc/letsencrypt/live/pyapps.site/cert.pem", "--https-certificate-key-file=/etc/letsencrypt/live/pyapps.site/privkey.pem"]
