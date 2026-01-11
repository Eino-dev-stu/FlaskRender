# App deployed using render
The app has a simple frontpage were the user can input a name.  Using free API's information is shown about the given name.
The backend is resposible for getting the data form free API's. 

Both frontend and backend are deployed as web services on Render.  This made using dockerfiles easier.
The app has a config file ci.yml that works as a deployment pipeline.  This might be a bit redundant because render updates from github automatically.

The links might take a while to work.  Free render has its limitations.
[Frontend Link](https://frontpage-xybs.onrender.com/data.html)
[Backend Link](https://flaskrender-en8x.onrender.com/)
