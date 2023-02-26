# FreJun-Python-Task
## CRUD API Implementation using Flask 

This API provides the solution to the task provided to me by FreJun.ai 


------------------------------------------------------------------------------------------
### Requirements to be satisfied
- <code>pip install flask</code> </br>
- <code>pip install mysql-connector-python</code>
- <code>pip install pandas</code></br>
- <code>pip install datetime</code>
#### To create a POST request to initiate-call and save the details in a MYSQL Database along with a <code>start_time</code> timestamp.

![image](https://user-images.githubusercontent.com/78322027/221423143-6d039977-3554-480d-b668-261deab6ae59.png)
<details>

 <summary><code>POST</code> <code><b>/</b></code> <code>(initiate-call)</code></summary>

##### Parameters
> None

##### Body Data for Postman Testing
<code>{
"from_number": "89XXXX1132",
"to_number": "62XXXXX232"
}
</code>

##### Responses

> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `201`         | `text/plain;charset=UTF-8`        | `success`                                |
> | `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}`                            |
> | `405`         | `text/html;charset=utf-8`         | None                                                                |

</details>

------------------------------------------------------------------------------------------

#### To create a GET request which fetches a call report from the db
![image](https://user-images.githubusercontent.com/78322027/221424151-1fc01c99-e094-4eed-b2da-c2741a6e58e6.png)


<details>
 <summary><code>GET</code> <code><b>/</b></code> <code>(callreport?phone=<num>?pagenumber=1)</code></summary>

##### Parameters

> | name      |  type     | data type               | description                                                           |
> |-----------|-----------|-------------------------|-----------------------------------------------------------------------|
> | /initiate-call      |  required | object (JSON or YAML)   | N/A  |

##### Responses

> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `200`         | `application/json'        | JSON String                                                       |

##### Output Screenshot
![image](https://user-images.githubusercontent.com/78322027/221424382-48cb8679-2ec0-411f-bd15-445f7f787b29.png)

</details>

------------------------------------------------------------------------------------------

