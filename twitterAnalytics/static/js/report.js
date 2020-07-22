function changeOptions(selectEl) {
    let selectedValue = selectEl.value;
    let subForms = document.getElementsByClassName('form-control')
    for (let i = 0; i < subForms.length; i += 1) {
      if (selectedValue === subForms[i].id) {
        subForms[i].setAttribute('style', 'display:inline')
      } 
      else {
        subForms[i].setAttribute('style', 'display:none') 
      }
    }
  }