function disableSubmit(whichButton) {
if (document.getElementById) {
document.getElementById(whichButton).disabled = true;
} else if (document.all) {
document.all[whichButton].disabled = true;
} else if (document.layers) {
document.layers[whichButton].disabled = true;
}
}