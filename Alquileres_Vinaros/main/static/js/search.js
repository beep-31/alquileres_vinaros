let check_out = document.querySelector('#check-out'),
    check_in = document.querySelector('#check-in');

check_out.addEventListener('click', ()=>{
    check_out.min = check_in.value;
})

check_in.addEventListener('click', ()=>{
    if(check_out.value == ''){
        check_in.max = ''
    } else{
        check_in.max = check_out.value
    }
    
})