# hello-fastapi-demo

This is just a quick demo on how to use fastapi and send messages. You can run the server with the command:

uv run fastapi dev .\app\app.py

When running you can access the started server at the displayed address, probably:

Server started at http://127.0.0.1:8000

You can also go to the provided documentation site and play with the echo message for example:

server   Documentation at http://127.0.0.1:8000/docs

A function to load files is provided as well, which you can use to send a file to the filecheck service. This should be the same for the frontend and backend communication later.
When you go to the docs server, you should see the functions under default. You can open them and use the 'Try it out' button. Depending on which you execute you get different results.
- Health doesn't take any parameters and should just display 
{
  "status": "UP",
  "message": "Service is running"
}
- In echo you can change the string in the parantheses to anything you want
{
  "message": "string"
}
and it should be displayed as 
{
  "message": "my message"
}
- uploadfile allows you to upload a file and display its type as well as if it is an mp3, for example
{
  "filename": "recording.wav",
  "content_type": "audio/wav",
  "message": "This is not an MP3 file."
}

Now to create a docker container for it you have to create a Dockerfile first. You can look at the one in this project, which should be pretty straightforward. Of course you can also use other package managers than uv. When you defined everything in your docker file, you can already create the container by using:

docker build -t hello-fastapi-demo .

'.' Specifies the current directory for the Docker build context.
To run the container use:

docker run -d --name my-fastapi-app -p 8000:8000 hello-fastapi-demo

After running your Docker container, access the application by visiting 'http://localhost:8000/docs' in your web browser or any API client to ensure the service is up and running. 
You can use:

docker ps

and 

docker logs my-fastapi-app

to get more info on your image.
You can also use the docker desktop app to manage your images.