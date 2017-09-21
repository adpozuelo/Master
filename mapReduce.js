/********************************************************
 * Return for each country:                             *
 *  1) Total number of tweets in the database           *
 *  2) The 5 users with most tweets                     *
 *  3) The 10 most used sortedWords                     *
 ********************************************************/

// Antonio Diaz Pozuelo - adpozuelo@uoc.edu
// RD - PRA - 30/04/2017

var m = function() {
	var key = this.place.country_code;
	var value = { count : 0,
			words : {},
			users : {} };
	if (this.place != null) {
		value.count = 1;
	}
	if (this.user.screen_name != null) {
		value.users[this.user.screen_name] = 1;
	}
	this.text.match(/\S+/g).forEach(function(word) {
		if ( word.length > 3 && ! word.match(/^http/) && word.match(/^[a-zA-Z]/) ) {
			if (word in value.words) {
				value.words[word] += 1;
			} else {
				value.words[word] = 1;
			}
		}})
	emit(key, value);
};

var r = function(key, values) {
	reducedVal = { count: 0,
			words: {},
			users: {} };
	values.forEach( function(value) {
		reducedVal.count += value.count;
		for (user in value.users) {
			if (user in reducedVal.users) {
				reducedVal.users[user] += value.users[user];
			} else {
				reducedVal.users[user] = value.users[user];
			}
		}
		for (word in value.words) {
			if (word in reducedVal.words) {
				reducedVal.words[word] += value.words[word];
			} else {
				reducedVal.words[word] = value.words[word];
			}
		}
	});
	return reducedVal;
};

var f = function(key, val) {
	finalizedVal = { count: val.count,
                        words: [],
			users: [] };
	var sortedWords = [];
  	for (var w in val.words) sortedWords.push(w);
	finalizedVal.words = sortedWords.sort(function(a,b) {return val.words[b]-val.words[a]}).slice(0,10);
	var sortedUsers = [];
        for (var u in val.users) sortedUsers.push(u);
        finalizedVal.users = sortedUsers.sort(function(a,b) {return val.users[b]-val.users[a]}).slice(0,5);
	return finalizedVal;
};

db.runCommand( {
                 mapReduce: "tweets",
                 map: m,
                 reduce: r,
                 finalize: f,
                 out: {replace : "result"}
               } );

// To show results: db.result.find().pretty()
//
// While testing, to reduce the execution time you can filter tweets for country.
// For example you could just calculate the results for Andorra:
//
// 1) Create an Index on country_code:
//
//    db.tweets.createIndex({"place.country_code": 1})
//
// 2) Add the filter to the map reduce:
//
//    db.runCommand( {
//                     mapReduce: "tweets",
//                     map: m,
//                     reduce: r,
//                     finalize: f,
//                     query: {"place.country_code":"AD"},
//                     out: {replace : "result"}
//                   } );
//
// 3) Check results:
//
//    > db.result.find().pretty()
//      {
//        "_id" : "AD",
//        "value" : {
//          "count" : 218,
//          "words" : [
//            "Andorra",
//            "Grandvalira",
//            "para",
//            "nieve",
//            "dels",
//            "informació",
//            "Casa",
//            "Gerard",
//            "d'Andorra",
//            "Escoda,"
//          ],
//          "users" : [
//            "12h15m",
//            "PeriodicAND",
//            "AndorraLovers",
//            "LiberalsAndorra",
//            "GovernAndorra"
//          ]
//        }
//      }
   
