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

Local results are available in:
	http://localhost:5601  
	
Benchmark results in:
	https://tdes-dev.tokbox.com:5601/app/kibana#/dashboard/[juanc352]-benchmark-Elastic-vs-Mongo?_g=%28refreshInterval:%28display:%275%20seconds%27,pause:!f,section:1,value:5000%29,time:%28from:now-7d,mode:quick,to:now%29%29&_a=%28filters:!%28%29,options:%28darkTheme:!f%29,panels:!%28%28col:1,id:[juanc352]-Times-Benchmark,panelIndex:1,row:1,size_x:9,size_y:5,type:visualization%29%29,query:%28query_string:%28analyze_wildcard:!t,query:%27*%27%29%29,title:%27[juanc352]%20benchmark%20Elastic%20vs%20Mongo%27,uiState:%28%29%29


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
