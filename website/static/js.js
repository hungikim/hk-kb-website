function deletePost(postId){
    fetch('/delete-post', {
        method: 'POST',
        body: JSON.stringify({ postId: postId })
    }).then( (res)=> {
        window.location.href = '/'; 
    });
}

function showUpdateForm(postId){
    let existingUpdateForm = document.getElementById('updateform');
    if (existingUpdateForm){ existingUpdateForm.remove(); }

    document.getElementById("update-form-"+postId).innerHTML = `
        <form id="updateform">
        <label><textarea id="update-text-area" class="text-area" required></textarea></label>
        <button class="btn-post" type="button" id="btn-update" onclick="updatePost(${postId})">Update</button>
        </form>
    `;
}

function updatePost(postId){
    fetch('/update-post', {
        method: 'POST',
        body: JSON.stringify({
            postId: postId,
            text: document.getElementById("update-text-area").value
        })
    }).then( (res) => {
        window.location.href = '/';
    });
}

function redirectToHome(){
    window.location.href = '/';
}

function darkMode(){

}

document.getElementById("main-header").onclick = redirectToHome;