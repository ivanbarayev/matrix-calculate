# matrix-calculate

### For notes please check the [NOTES.md](NOTES.md)
### For build log on RisingCloud platform side please check the [Build.log](Build.log)


# 1. Install the Rising Cloud Command Line Interface (CLI)
In order to run the Rising Cloud commands in this guide, you will need to [install](https://risingcloud.com/docs/install) the Rising Cloud Command Line Interface. This program provides you with the utilities to setup your Rising Cloud Task or Web Service, upload your application to Rising Cloud, setup authentication, and more.

# 2. Login to Rising Cloud Using the CLI
```shell
make login
```

# 3. Initialize Your Rising Cloud Task
```shell
make init
```

This creates a risingcloud.yaml file in your project directory. This file can be used to configure the build script.

# 4. Create Your Rising Cloud Task

```
matrix_calc.py
```

**Configure your risingcloud.yaml**

Check the `risingcloud.yaml ` file for configurations

# 5. Build and Deploy Your Rising Cloud Task

Created a Makefile, for more detail please check the `Makefile`

```shell
make deploy
```

**Make requests**

Making a request with a JSON body of:
```shell
POST
https://matrix-calculate.risingcloud.app/risingcloud/jobs

BODY:
{"A":[[2,4],[6,8]],"B":[[1,3],[5,7]]}
```

should cause the "result" field in a completed Job Status to be (in result.json file):

```
# Success 
{"error": false, "messages": null, "result": [[22, 34], [46, 74]]}

# Error
{"error": true, "messages": ["First Matrix array is not valid !"], "result": null}
```