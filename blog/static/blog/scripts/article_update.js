 function update() {
    homes = $("#home");
    most_recent = homes.find('div:first');
    $.getJSON("article-after/" +  most_recent.attr("id")+ "/",
        function(data){
            cycle_class = most_recent.hasClass("odd")
                ? "even" : "odd";
            jQuery.each(data, function(){
                homes.prepend(
                    '<div id="'+ this.pk +'" class="col-xs-12 col-md-6 home '+cycle_class+'">' +
                    '<h4 id="title">' +
                    '<a href="/article/'+this.pk+'">'+this.fields.article_title+'</a>'+
                    '</h4>' +
                    '<p class="text-muted">' +
                    '<small>'+this.fields.article_date+'' +
                    '</small></p>' +
                    '<div class="article_text">' +
                    '<p>' +this.fields.article_text +'</p>' +
                    '<a href="/article/'+this.pk+'">></a></div></hr></div>'
                );
                cycle_class = (cycle_class == 'odd')
                    ? "even" : "odd";
            });
        });
}
$(document).ready(function(){
    setInterval("update()", 60000);

});
$("#title").click(function(){
    alert("Click title")
});