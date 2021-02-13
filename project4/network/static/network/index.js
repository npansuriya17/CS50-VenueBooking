document.addEventListener('DOMContentLoaded', function () {

    var btn_post = document.getElementById('btn-new-post');
    btn_post.disabled = true;

    document.querySelector('#new-post-content').onkeyup = () => {
        if (document.querySelector('#new-post-content').value.trim().length > 0) {
            btn_post.disabled = false;
        }
        else {
            btn_post.disabled = true;
        }
    };

});

function like_unlike(liked) {
    if (liked === "like") {
        alert(liked);
    } else if (liked === "unlike") {
        alert(liked);
    }
}


function logout() {
    sessionStorage.clear();
    localStorage.clear();
}

function load_allposts(posts) {
    var new_post = document.querySelector('#tr-new-post');
    //var allposts = document.querySelector('#tr-allposts');
    var btn_post = document.getElementById('btn-new-post');
    new_post.style.display = 'block';
    //allposts.style.display = 'block';
   
    btn_post.disabled = true;
    document.querySelector('#new-post-content').onkeyup = () => {
        if (document.querySelector('#new-post-content').value.length > 0) {
            btn_post.disabled = false;
        }
        else {
            btn_post.disabled = true;
        }
    };
    btn_post.addEventListener("click", () => newpost())

    fetch(`/allposts`)
	.then(response => response.json())
	.then(posts => {
		if (posts.length == 0) {
			allposts.innerHTML = '<td><p style = "font-size: large; font-weight: bold;">Nothing to see here :( </p></td>';
		}
		else {
            var posts_table = document.querySelector('#posts-table');
            posts_table.innerHTML = "";
            for (post in posts) {
                var post_row = document.createElement("tr");
                var post_data = document.createElement("td");
				var user_name = document.createElement('p');
				var post_content = document.createElement('p');
				var post_time = document.createElement('p');
                var likes = document.createElement('p');
                
                user_name.innerHTML = posts[post]['posted_by_user'];
                post_content.innerHTML = posts[post]['content'];
                post_time.innerHTML = posts[post]['posted_time'];

                
                posts_table.appendChild(post_row);
                post_row.appendChild(post_data);
                post_data.appendChild(user_name);
                post_data.appendChild(post_content);
                post_data.appendChild(post_time);
            }
        }
    });
};

function load_posts(profile) {
    event.stopImmediatePropagation();
    document.querySelector('#tr-new-post').style = 'none';
    //var allposts = document.querySelector('#tr-allposts');

    //allposts.style.display = 'block';

    fetch(`/allposts/${profile}`)
	.then(response => response.json())
	.then(posts => {
		if (posts.length == 0) {
			allposts.innerHTML = '<td><p style = "font-size: large; font-weight: bold;">Nothing to see here :( </p></td>';
		}
		else {
            var posts_table = document.querySelector('#posts-table');
            posts_table.innerHTML="";
            for (post in posts) {
                var post_row = document.createElement("tr");
                var post_data = document.createElement("td");
				var user_name = document.createElement('p');
				var post_content = document.createElement('p');
				var post_time = document.createElement('p');
                var likes = document.createElement('p');
                
                user_name.innerHTML = posts[post]['posted_by_user'];
                post_content.innerHTML = posts[post]['content'];
                post_time.innerHTML = posts[post]['posted_time'];

                posts_table.appendChild(post_row);
                post_row.appendChild(post_data);
                post_data.appendChild(user_name);
                post_data.appendChild(post_content);
                post_data.appendChild(post_time);

            }
        }
    });
};

function newpost() {
    var post_content = document.querySelector('#new-post-content').value;
    fetch(`/newpost`,{
        method: 'POST',
        body: JSON.stringify({
            content:post_content
        })
    })
    .then(response => response.json())
    .then(result => {
        console.log(result);
    })
};