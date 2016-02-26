ElasticMongo  
===========  
ElasticMongo is a project to compare PyMongo with ElasticSearch. This benchmark shows the performance of both connectors.

ElasticSearch  
--------------  
Installed in C:\elasticsearch-2.1.1\bin  

data:  
	C:\elasticsearch-2.1.1\data  


Kibana  
-------  
Kibana is installed in C:\kibana-4.3.1-windows\bin  

Results are available in http://localhost:5601  


MongoDB  
--------  
Installed in C:\Program Files\MongoDB\Server\3.2\bin

start server:  
	"C:\Program Files\MongoDB\Server\3.2\bin"\mongod  
	
start client:  
	"C:\Program Files\MongoDB\Server\3.2\bin"\mongo  
	
data:  
	C:\data\db  
	 
clean cache in mongo:  
	db.demo.getPlanCache().clear()  
  
To use '$text' search, a text index has been create on body field
db.mongo.createIndex( { body: "text" } )
