//Switch to certain nav (string for tab - which is the tab id name)
function activate_tab(tab){
	$('.nav-tabs a[href="#' + tab + '"]').tab('show');
};
