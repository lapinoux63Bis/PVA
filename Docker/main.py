import docker

client = docker.from_env()

if client.containers.list(filters={"name": "ReceiverTest"}):
    container = client.containers.get("ReceiverTest")
    container.stop()
    print("ReceiverTest stopped")
    container.remove()
    print("ReceiverTest removed")

print("Build image...")
client.images.build(path="Container/", buildargs={"-t": "python_receiver"})
print("Run container...")
client.containers.run("python_receiver", detach=True, ports={'12345/udp': 12345, '12346/udp': 12346}, name="ReceiverTest")
print("Done.")
