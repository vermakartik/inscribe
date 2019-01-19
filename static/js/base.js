function show_menu(){
	console.log("click called!")
	let menuListElement = document.getElementById("menu_list");
	console.log(menuListElement);
	if(menuListElement.style.display === "block"){
		console.log("called None");
		menuListElement.style.display = "none";
	} else {
		console.log("called block");
		menuListElement.style.display = "block";
	}
}