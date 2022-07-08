## Installation
Run docker compose:
```
docker-compose up
```


## Using kafka
create topic test:
```
docker exec broker kafka-topics --bootstrap-server broker:9092 --create --topic test
```

list topics:
```
docker exec broker kafka-topics --bootstrap-server broker:9092 --list
```

write to topic test (Ctrl + C to exit):
```
docker exec -it broker kafka-console-producer --broker-list broker:9092 --topic test
```

to see message logs:
```
docker exec broker kafka-run-class kafka.tools.DumpLogSegments --deep-iteration --print-data-log --files /var/lib/kafka/data/test-0/00000000000000000000.log
```

to consume messages (Ctrl + C to exit):
```
docker exec broker kafka-console-consumer --bootstrap-server broker:9092 --topic test --from-beginning
```


## Links
[https://developer.confluent.io/quickstart/kafka-docker/](https://developer.confluent.io/quickstart/kafka-docker/)

[https://towardsdatascience.com/getting-started-with-apache-kafka-in-python-604b3250aa05](https://towardsdatascience.com/getting-started-with-apache-kafka-in-python-604b3250aa05)

[https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html)


