# Docker Compose 'hello world' Example

The aim here is to create a basic Docker Compose example. Lon/lat coordinate points
are added through an API by a user, and then plotted on a map displayed on a dashboard.

## Design

There are two simple services comprising of a 'backend' REST API built with FastAPI, 
and a 'frontend' dashboard built with Dash and Folium.

Data is input using the REST API and stored in a SQLite database. A GET endpoint allows
the records the database to be accessed by the dashboard service via a URL. The request
is made through the API and the data is plotted on a Folium map within the dashboard.