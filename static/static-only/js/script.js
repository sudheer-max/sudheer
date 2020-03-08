<script>
$(function(){

    'use strict';
    $('ul.filters > li').on('click', function(e){
      e.preventDefault();
      $('ul.filters > li').removeClass('active');
      $(this).addClass('active');
    });
})(jQuery);
</script>