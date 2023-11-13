<!DOCTYPE html>
<html>
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script>
$(document).ready(function(){
    $("#hide").click(function(){
        $("div").hide();
    });
});
</script>
</head>
<body>

<div>If you click on the "Hide" button, I will disappear.</div>

<button id="hide">Hide</button>
</body>
</html>