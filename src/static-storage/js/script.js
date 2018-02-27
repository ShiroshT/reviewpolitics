var scoreUp, scoreDown,  scoreNet, activeBtn, valueUpdated;


scoreUp =0;
scoreDown = 0
scoreTotal = 0;
activeBtn = 0;

valueUpdatedUp = false;
valueUpdatedDown = false;

// take the current value - from the database - Need to figure out how to do this
scoreNet = Math.floor(Math.random() *10);

document.querySelector('#score-net').textContent = scoreNet;



// update the value based on the button 
function calculate(){
			if (scoreUp === 0 && scoreDown === 0){
				scoreUp =1;
				scoreDown = 0;
				scoreNet = scoreNet + scoreUp;
				document.querySelector('#score-net').textContent = scoreNet;
			}
			else if (scoreDown === 0 && scoreUp === 0 ){
				scoreDown =1;
				scoreUp =0;
				scoreNet = scoreNet -  scoreDown;
				document.querySelector('#score-net').textContent = scoreNet;
			}		
};

document.querySelector('#score-up-detail').addEventListener('click', function(){
		calculate();
});


document.querySelector('#score-down-detail').addEventListener('click', function(){
		calculate();
});



