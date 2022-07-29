# json-xml-api-endpoint #

Since the Personio API doesn't provide a developer mode, i created this little docker application to simulate the /v1/company/employees endpoint of the API, as well as the {companyName}.jobs.personio.de/xml site, where job offers are being serialized in xml. As you can pass your own data, you can use this container to create a xml and json GET-endpoint with any data.

## Build and run the container

```sh
docker build -t my-personio-mockup .

docker run -d -p 8080:80 nameOfDockerbuild
```

## Using your own Data

This Repo comes preconfigured with two employees and the content of [test.jobs.personio.de/xml](https://test.jobs.personio.de/xml). If you want to pass your own data, create a folder and make two files (one for xml and one for json), where you can store your own information.

```sh
mkdir ownData

touch ownData/data.json && touch ownData/data.xml

docker run -d -p 8080:80 -v /path/to/ownData:/app/data nameOfDockerbuild
```

After choosing one of the two methods above, you should see a confirmation at [127.0.0.1:8080](http://127.0.0.1:8080) that the server is running.

You can now make GET-Calls to [127.0.0.1:8080/json](http://127.0.0.1:8080/json) or [127.0.0.1:8080/xml](http://127.0.0.1:8080/xml)
