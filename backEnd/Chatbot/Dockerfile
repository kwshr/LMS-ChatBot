FROM maven:3.8.5-openjdk-17 AS build
COPY /src /home/app/src
COPY /pom.xml /home/app
RUN mvn -f /home/app/pom.xml clean package

FROM openjdk:17

ARG JAR_FILE=target/*.jar

COPY ./target/Chatbot-0.0.1-SNAPSHOT.jar app.jar

ENTRYPOINT ["java", "-jar", "app.jar"]








