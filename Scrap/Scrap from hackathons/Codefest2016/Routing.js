
var __stupid_global_variable$Anjali33Adeeb = false;
function calculateAndDisplayRoute(start, end, obstructions, directionService, rend, OK, waypts) { 
  var wp = [];
  waypts.forEach(function(e){return {location: e, stopover: true};});
  
  directionService.route({
    origin: start,
    destination: end,
	waypoints: wp,
	optimizeWaypoints: true,
    travelMode: google.maps.TravelMode.WALKING
  },
	function(response, status) {
		
		if (status === OK) {
			var fix = isClear(obstructions, response);
			alert(Object.keys(fix));
			if(Object.keys(fix).length === 0){
				__stupid_global_variable$Anjali33Adeeb = true;	
				rend.setDirections(response);
			}else if(waypts.length === 0){
				var perms = choices(fix);
				for(var i = 0; i < perms.length; i++){
					calculateAndDisplayRoute(start, end, obstructions, 
						directionsService, directionRenderer, OK, fix[i]);
					if (__stupid_global_variable$Anjali33Adeeb === true)
						return;
				}
			}	
		} else {
			window.alert('Directions request failed due to ' + status);
		}
	} 
	  // for each combination of fix which is list of lists of waypoints, recur 
	  // and recur only this once
	  //if that combo gets a valid path, then with global var, don't continue recur calls
	  // if that fails, then screw the handicapped, none of the approximate solutions failed
	);
}

function choices(fix){
	var scats = [];
	for(var key in fix){
		acc.push(fix[key]);
	}
	
	var acc = [], rv = [];
	scat.forEach(function(e){
		acc.push(0);
	});
	
	var ind = 0;
	while(acc[ind] < scats[ind].length || ind < scats.length){
		if(ind < scats.length){
			acc[ind] = 0;
			ind++;
			acc[ind]++;
		}else{
			var t = [], i = 0;
			acc.forEach(function(e){
				t.push(scats[i][e]);
				i++;
			});
			rv.push(t);
			acc[0]++;
			ind = 0;
		}
	}
	return rv;
}

function testIntersect(wp1, wp2, obs){
	var m = (wp2.lat()-wp1.lat())/(wp2.lng()- wp1.lng());
	var ob = [obs.lng,obs.lat];
	return (Math.abs(-m*ob[0] + ob[1] + m*wp1.lng() - wp1.lat() )) < 0.08 * Math.sqrt(m*m + 1); // eyeballing the significatn difference
	
}

function isClear(obstructions, directions){
	
	var wps = directions.routes[0].overview_path;
	alert(wps);
	var scat = {};
	for(var i=0;i<(wps.length-1);i++){
		obstructions.forEach(function(obs){
			if(testIntersect(wps[i], wps[i + 1], obs)){
				alert('ti wrk');
				scat[obs.id + ''] = (scatters([obs.lat, obs.lng])); // scatters given a obs point, will return an array of waypoints per that obs
			}	
		});
	}
	return scat;
}

function scatters(wp){
	var r = .09;
	return [[wp[0]+r,wp[1]],
			[wp[0]-r,wp[1]],
			[wp[0],wp[1]+r],
			[wp[0],wp[1]-r]];
	
}



