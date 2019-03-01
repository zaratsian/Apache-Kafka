

##############################################################################
#
#   Kafka - Encryption and Authentication using SSL
#
#   Reference:
#       https://kafka.apache.org/documentation/#security
#
##############################################################################

# Generate SSL key and certificate for each Kafka broker
keytool -keystore server.keystore.jks -alias localhost -validity 365 -genkey -keyalg RSA

# Verify the contents of the generated certificate
keytool -list -v -keystore server.keystore.jks

# Generate a CA (certificate authority)
openssl req -new -x509 -keyout ca-key -out ca-cert -days 365

# Add the generated CA to the **server's truststore** so that the server can trust this CA
keytool -keystore server.truststore.jks -alias CARoot -import -file ca-cert
# Add the generated CA to the **client's truststore** so that the client can trust this CA
keytool -keystore client.truststore.jks -alias CARoot -import -file ca-cert

##############################################################################
# Sign all certificates
##############################################################################

# (1) Export the certificate from the keystore
keytool -keystore server.keystore.jks -alias localhost -certreq -file cert-file

# (2) Then sign it with the CA
openssl x509 -req -CA ca-cert -CAkey ca-key -in cert-file -out cert-signed -days 365 -CAcreateserial -passin pass:password

# (3) Import both the certificate of the CA and the signed certificate into the keystore
keytool -keystore server.keystore.jks -alias CARoot -import -file ca-cert
keytool -keystore server.keystore.jks -alias localhost -import -file cert-signed

##############################################################################
# Edit server.properties
##############################################################################
listeners=PLAINTEXT://kafka-secure-vm:9092,SSL://kafka-secure-vm:9093
ssl.keystore.location=/home/dzaratsian/server.keystore.jks
ssl.keystore.password=password
ssl.key.password=password
ssl.truststore.location=/home/dzaratsian/server.truststore.jks
ssl.truststore.password=password

##############################################################################
# Example - Kafka Producer (for Testing)
##############################################################################
/kafka/bin/kafka-console-producer.sh --broker-list kafka-secure-vm:9093 --topic eye_tracking --producer.config /kafka/config/client-ssl.properties



#ZEND
