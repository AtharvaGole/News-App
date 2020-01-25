var total_posts = 3;
var category = "";
var country = "us";
var q = "";
var url = "http://localhost:5000";

var load_more_state = 0;


function set_category(ca) {
	category = ca;
	console.log(category);
}


function set_country(co) {
	country = co;
	console.log(country);
}


function set_parameters(ca, co) {
	category = ca;
	country = co;
	console.log(ca+" "+co);
}


function increment_posts() {
	total_posts++;
	console.log(total_posts);
}



function get_html(row) {
	return '<div class="row mb-2"><div class="col-md-12"><div class="card flex-md-row mb-4 box-shadow h-md-200"><div class="card-body d-flex flex-column align-items-start"><h3 class="mb-0">'+row["title"]+'</h3><div class="mb-1 text-muted">'+row["publishedAt"]+'</div><a href="#">Continue reading</a></div><img class="card-img-right flex-auto d-none d-md-block" width="200px" height="150px" src="'+row["urlToImage"]+'" alt="Card image cap"></div></div></div>';
}


function load_more() {
	
	if(load_more_state == 0) {

		$.getJSON(url+"/load_more?total_posts="+total_posts+"&category="+category+"&country="+country, 
					function(data,textStatus,jqXHR) {
						
						if(data["data"].length == 0) {
							document.getElementById("load_more").style.visibility = "hidden";
							return;
						}

						for(var row_no in data["data"]) {
							total_posts++;
							row = data["data"][row_no];
							console.log(total_posts);
							document.getElementById("blog-post").innerHTML += get_html(row);
							//document.getElementById("extra_posts").innerHTML = "asds";
						}
					}
				
				)

	}
	else {

			$.getJSON(url+"/search_articles?total_posts="+total_posts+"&q="+q, 
					function(data,textStatus,jqXHR) {
						
						if(data["data"].length == 0) {
							document.getElementById("load_more").style.visibility = "hidden";
							return;
						}

						for(var row_no in data["data"]) {
							total_posts++;
							row = data["data"][row_no];
							console.log(total_posts);
							document.getElementById("blog-post").innerHTML += get_html(row);
							//document.getElementById("extra_posts").innerHTML = "asds";
						}
					}
				
				)

	}
	
}



function load_category(ca) {

	category = ca;
	load_more_state = 0;

	$.getJSON(url+"/load_category?total_posts="+total_posts+"&category="+category+"&country="+country, 
				function(data,textStatus,jqXHR) {

					total_posts = 3;
					
					document.getElementById("load_more").style.visibility = "visible";
					
					document.getElementById("blog-post").innerHTML = "";

					for(var row_no in data["data"]) {
						total_posts++;
						row = data["data"][row_no];
						console.log(total_posts);
						document.getElementById("blog-post").innerHTML += get_html(row);
						//document.getElementById("extra_posts").innerHTML = "asds";
					}
				}
			
			)

}


function load_country() {
	
	country = document.getElementById("country_drop_down").value;
	load_more_state = 0;

	$.getJSON(url+"/load_category?total_posts="+total_posts+"&category="+category+"&country="+country, 
				function(data,textStatus,jqXHR) {

					total_posts = 3;
					
					document.getElementById("load_more").style.visibility = "visible";
					
					document.getElementById("blog-post").innerHTML = "";

					for(var row_no in data["data"]) {
						total_posts++;
						row = data["data"][row_no];
						console.log(total_posts);
						document.getElementById("blog-post").innerHTML += get_html(row);
						//document.getElementById("extra_posts").innerHTML = "asds";
					}
				}
			
			)

}


function search_articles() {

	q = document.getElementById("search_articles").value;
	load_more_state = 1;
	
	$.getJSON(url+"/search_articles?total_posts="+total_posts+"&category="+category+"&country="+country+"&q="+q, 
				function(data,textStatus,jqXHR) {

					total_posts = 0;
					
					document.getElementById("load_more").style.visibility = "visible";
					
					document.getElementById("blog-post").innerHTML = "";

					for(var row_no in data["data"]) {
						total_posts++;
						row = data["data"][row_no];
						console.log(total_posts);
						document.getElementById("blog-post").innerHTML += get_html(row);
						//document.getElementById("extra_posts").innerHTML = "asds";
					}
				}
			
			)
}
