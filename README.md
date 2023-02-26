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

```shell
GET
https://matrix-calculate.risingcloud.app/risingcloud/jobs/89604f46-ca58-45b2-bcde-d87821e26fb5

RESPONSE
{
    "id": "89604f46-ca58-45b2-bcde-d87821e26fb5",
    "status": "Completed",
    "worker": "63fb7b006d6fdb25cd90b342",
    "team": "63fb4252b846d7ad3f4a328f",
    "task": "63fb47410c1c289c647ebe81",
    "task_url": "",
    "key": "mcw4hmtpyet2dxkokdgro9a2g60ikkj7fh03nx",
    "input": {
        "A": [[2,4],[6,8]],
        "B": [[1,3],[5,7]]
    },
    "result": {
        "error": false,
        "messages": null,
        "result": [[22,34],[46,74]]
    },
    "stdout": "",
    "stderr": "",
    "error": "",
    "queueTime": "2023-02-26T15:29:49.933114385Z",
    "startTime": "2023-02-26T15:30:45.330658732Z",
    "endTime": "2023-02-26T15:30:45.710181953Z",
    "metrics": {
        "cpuPeak": 2.8237829601802455,
        "cpuMean": 1.254253052393338,
        "cpu_std_deviation": 1.133867473841392,
        "ramPeak": 34.1015625,
        "ramMean": 31.8671875,
        "ram_std_deviation": 2.565989034136212,
        "gpuPeak": 0,
        "gpuMean": 0,
        "gpu_std_deviation": 0,
        "timeSamples": [
            {
                "time": "2023-02-26T15:30:46.013413914Z",
                "ram": 32.55859375,
                "cpu": 2.8237829601802455,
                "gpu": 0
            },
            {
                "time": "2023-02-26T15:30:46.174302949Z",
                "ram": 32.640625,
                "cpu": 0.11408367885356513,
                "gpu": 0
            },
            {
                "time": "2023-02-26T15:30:46.207434562Z",
                "ram": 34.1015625,
                "cpu": 1.0658480466978772,
                "gpu": 0
            },
            {
                "time": "2023-02-26T15:30:46.276156369Z",
                "ram": 28.16796875,
                "cpu": 1.0132975238416644,
                "gpu": 0
            }
        ]
    }
}


RAW REQUEST AND RESPONSE
# Success 
{"error": false, "messages": null, "result": [[22, 34], [46, 74]]}

# Error
{"error": true, "messages": ["First Matrix array is not valid !"], "result": null}
```