index = 1;
			
function animate() {
	current = document.getElementById('current'); 
	current.id = 'hide' 
	img = document.getElementsByTagName('img');
	img[index].id = 'current';
	index ++;
	if (index < img.length) { 
		setTimeout(animate, 1000);
	}
}
	
