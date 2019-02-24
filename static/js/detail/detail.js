$(document).ready(function(){
    var a =""
	$("tt").css("color", "braun");
	a = $("tt").text();
	
	 $(".yorumlar").click(function(){
		 if($(this).text()!=0){
				$(this).next().toggle();
		 } 
        
    });
	
	 $(".aaa").click(function(){
		 
				$(this).hide();
		 
        
    });
	
	$(".kenar").click(function(){
        $(this).children('.truncate').toggle();
		$(this).children('.gizli').toggle();
		 
    });
	
	$(".mac").click(function(){
        $(this).children('.ayrinti').toggle();
		
		 
    });
	
	   $(".maclarım").click(function(){
        $(this).children('tr').toggle();
		$(this).children('.goster').show();
		 
    });
	
    
});