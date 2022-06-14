# Personio-API-Mockup #

Since the Personio API doesn't provide a developer mode, i created this little docker application to simulate the /v1/company/employees endpoint of the API, as well as the {companyName}.jobs.personio.de/xml site, where job offers are being serialized in xml.

```sh
docker build -t my-personio-mockup .

docker run -d -p 8080:80 my-personio-mockup
```

## Using your own Data

This Repo comes preconfigured with two employees and the content of [test.jobs.personio.de/xml](https://test.jobs.personio.de/xml). If you want to pass your own data, create a folder and make these two files, where you can store your own information.

```sh
mkdir ownData

touch ownData/employees.json && touch ownData/jobs.xml

docker run -d -p 8080:80 -v /path/to/ownData:/app/data my-personio-mockup
```

After choosing one of the two methods above, u should see a confirmation at 127.0.0.1:8080 that the server is running.

You can now make GET-Calls to [127.0.0.1:8080/v1/company/employees](http://127.0.0.1:8080/v1/company/employees) or [127.0.0.1:8080/xml](http://127.0.0.1:8080/xml)