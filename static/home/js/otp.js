$(document).ready(function () {
    $("#phone").intlTelInput({
      separateDialCode: true,
    });
  });
  
  function generateOTP() {
    var phoneNumber = $("#phone").intlTelInput("getNumber");
    var appointmentDate = $("#date").val();
    $("#genOtpBtn").css("display", "none");
    $("#resendOtp").css("display", "block");
    $("#otp-section").show();
    $("#bookBtn").show();
  }