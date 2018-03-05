// ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
// this is used to obtaine the search results from the API
// ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


// search query being obtained

function getParameterByName(name, url) {
    if (!url) {
      url = window.location.href;
    }
    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, " "));
}


//this whole part is done for the search results only.

// Start
$(document).ready(function(){
	console.log('JQ Working');
    var query = getParameterByName('q')
    var candidateList = [];
    var nextCandidateUrl;

    function candidateAttach(value){
		var candidateId = value.candidate_id;
		var candidateName = value.candiate_name; 
		var candidateSummary = value.summary_wiki;

		var candidateHtmlForm ="<div class=\"media\"><div class =\"media-left\">" 
		 + candidateName 	+ "<br/>"
		 + candidateSummary + "<br/>"
		 +"<a href='#'> See details </a>"
		 +"</div> </div><hr/>";
	    $("#candidate-search-results").append(candidateHtmlForm);

    }

	function parseCandidates(){
		if (candidateList == 0) {
			$("#candidate-search-results").text("No Candidates availble by that name")
		} else 
		// if candidate name exsist display the candidate
		 {
				$.each(candidateList , function(key, value)
				{		
						candidateAttach(value)	
				})
		 }	

	}

	function fetchCandidate(url)
		{

			var fetchUrl;


			if (!url) {
				fetchUrl = '/api/candidates/';
			} else {
				fetchUrl = url;
			}
			console.log("fetching candidates...");
			$.ajax({
			    url: '/api/candidates/',
			    data: {
			    	"q":query
			    },
			    method: 'get', // This is the default though, you don't actually need to always mention it
			    success: function(data) {
			    	candidateList = data.results;
			    	if(data.next) {
			    		nextCandidateUrl = data.next
			    	} else {
			    		$('#loadmore-candidates-search-results').css("display", "none")
			    	}
			    	
			    	parseCandidates();
			    },
			    failure: function(data) { 
			        alert('Got an error dude');
			    }
			}); 
	   }
	   fetchCandidate()

	   $('#loadmore-candidates-search-results').click(function(event) {
	   		event.preventDefault()
	   		if(nextCandidateUrl){
	   			 fetchCandidate(nextCandidateUrl)
	   		}
	   })



}); // end


// this part is for the search where when you type the search resutls are retrived automatically - Autosearching

$(document).ready(function(){
	var typingTimer;
	var doneInterval = 500;
	var searchInput = $("#main-search-form input[type=text]");
	var searchQuery;


	searchInput.keyup(function(event){
		searchQuery = $(this).val();
		clearTimeout(typingTimer);
		typingTimer = setTimeout(doneSearchTypying, doneInterval); 

	})

	searchInput.keydown(function(event){
		clearTimeout(typingTimer);
	})

	function doneSearchTypying(){
		if (searchQuery){
			// do search
			var url = '/candidates/search/?q=' + searchQuery;
			document.location.href =url;

		}

	}

})





// var scoreUp, scoreDown,  scoreNet, activeBtn, valueUpdated;
// scoreUp =0;
// scoreDown = 0
// scoreTotal = 0;
// activeBtn = 0;

// valueUpdatedUp = false;
// valueUpdatedDown = false;

// take the current value - from the database - Need to figure out how to do this
// scoreNet = Math.floor(Math.random() *10);

// document.querySelector('#score-net').textContent = candidateName;



// // update the value based on the button 
// function calculate(){
// 			if (scoreUp === 0 ){
// 				scoreUp =1;
// 				scoreDown = 0;
// 				scoreNet = scoreNet + scoreUp;
// 				document.querySelector('#score-net').textContent = scoreNet;
// 			}
// 			else if (scoreDown === 0 ){
// 				scoreDown =1;
// 				scoreUp =0;
// 				scoreNet = scoreNet -  scoreDown;
// 				document.querySelector('#score-net').textContent = scoreNet;
// 			}		
// };

// document.querySelector('#score-up-detail').addEventListener('click', function(){
// 		calculate();
// });


// document.querySelector('#score-down-detail').addEventListener('click', function(){
// 		calculate();
// });



