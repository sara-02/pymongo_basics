* MongoDB allows text search queries. The key/s over which the query is performed sow be an index, more specifically a text index. There can only be one text index per collection, but that text index can have any number of fields.

* The $text operation performs logical oring of the elements in the $search operation.

* Term exlusion cna be performed using -. The hypen between terms is exlcuded. 

* Although the result is in unsorted order, the system perform relevance scoring on the matched documents. SO we can sort our results accordingly

* the find() operation return an object of type 'pymongo.cursor.Cursor'.

* The default langiage for the search is English(i.e stemming and stop word removal is performed in English). To specify any otehr language set the default_langauge=specific language while creating the text index.

* Incase of multiple language in the document, specifiy the language field in the embedded document, and it will be given preference while indexing. Also can you specify the language override option, if hte langauage is tored in a dofferent key.

* The text index is created by contactinating the names of the required fields together each ending with the word _text. This must fall within the index name length limit. To specify a new name for the index, set the name property while creating the index.

* We can store the result of the update/remove query to see the number of matched counts.



