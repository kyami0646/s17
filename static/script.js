$(".openbtn").click(function () {
	$(this).toggleClass('active');
    $("#g-nav").toggleClass('panelactive');
});

$("#g-nav a").click(function () {
    $(".openbtn").removeClass('active');
    $("#g-nav").removeClass('panelactive');
});


// モーダルウィンドウ
$(function () {
    $(".js-modal-open").on("click", function () {
      $(".js-modal").fadeIn();
      return false;
    });
    $(".js-modal-close").on("click", function () {
      $(".js-modal").fadeOut();
      return false;
    });
  });
  // モーダルウィンドウオープン時の背景固定
  $(function () {
    let scrollPosition;
    $(".js-modal-open").on("click", function () {
      scrollPosition = $(window).scrollTop();
      $("body").addClass("fixed").css({ top: -scrollPosition });
    });
    $(".js-modal-close").on("click", function () {
      $("body").removeClass("fixed").css({ top: 0 });
      window.scrollTo(0, scrollPosition);
    });
  });
  