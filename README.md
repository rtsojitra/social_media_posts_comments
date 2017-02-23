# social_media_posts_comments

This project is to give an idea of how social media posts comments would look like. It can have more fields in the column. Below will how document would look like after executing this script.


below is an example of one of the document that stores post and its comments:



	{
			"_id" : ObjectId("58ae3483f545d12348b0d12c"),
			"text" : "Hello!!! Morning Friends!",
			"author" : {
					"id" : ObjectId("58ae3483f545d12348b0d12b"),
					"name" : "Aarti"
			},
			"posted" : ISODate("2017-02-22T20:01:55.838Z"),
			"comments" : [ 
					{
							"text" : "GM! How are you??",
							"user_id" : "ObjectId('58ae26c7f545d1185c29311e')",
							"posted" : ISODate("2017-02-22T20:01:55.839Z")
					}, 
					{
							"text" : "Hey, I am fine, how are you?",
							"user_id" : "ObjectId('58ae2fecf545d1132025a045')",
							"posted" : ISODate("2017-02-22T20:01:55.839Z")
					}
			]
	}
