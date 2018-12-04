$('#selectPageForm').submit(function(event)
{
	$('#selectPageForm').attr('action', $('#selectPageForm').attr('action')+"?curPage="+$('#curPage').val());
});