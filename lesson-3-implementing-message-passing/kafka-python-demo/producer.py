from kafka import KafkaProducer


TOPIC_NAME = 'items'
KAFKA_SERVER = 'my-release-kafka.default.svc.cluster.local:9092'

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

producer.send(TOPIC_NAME, b'Test Message!!!')
producer.flush()
