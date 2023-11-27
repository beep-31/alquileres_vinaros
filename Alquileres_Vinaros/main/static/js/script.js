const email_input = document.querySelector('#input__email'),
	email_label = document.querySelector('#email__label'),
	name_input = document.querySelector('#input__name'),
	name_label = document.querySelector('#name__label'),
	title_input = document.querySelector('#input__title'),
	title_label = document.querySelector('#title__label'),
	message_input = document.querySelector('#textarea'),
	message_label = document.querySelector('#textarea_label'),
	langBtn = document.querySelector('#drop-btn'),
	langDropDown = document.querySelector('#dropdown-menu'),
	mobile_menu = document.querySelector('#mobile-nav-panel'),
	mobile_menu_open_btn = document.querySelector('#nav-open'),
	mobile_menu_close_btn = document.querySelector('#nav-close');
	
mobile_menu_open_btn.addEventListener('click', function(){
	mobile_menu.style.right = '0px';
});

mobile_menu_close_btn.addEventListener('click', function(){
	mobile_menu.style.right = '-60vw';
});

let isDropped = false;
const opened = 'opened',
	  closed = 'closed';
	
langBtn.addEventListener('click', function(){
	if(isDropped == false){
		langDropDown.classList.remove('closed');
		langDropDown.classList.add('opened');
		isDropped = true;
	} else {
		langDropDown.classList.remove('opened');
		langDropDown.classList.add('closed');
		isDropped = false;
	}
});
	
	
email_input.addEventListener('focusout', function(){
    if(!email_input.checkValidity()){
        email_input.style.borderColor = 'red';
        email_label.style.color = 'red';
        email_label.style.top = '-10px';
        email_label.style.fontSize = '12px';
    } else {
        email_input.style.borderColor = '#A0D8B3';
        email_label.style.color = '#A0D8B3';
        email_label.style.top = '-10px';
        email_label.style.fontSize = '12px';
    }

    if(email_input.value == ''){
        email_input.style.borderColor =  '#0000001f';
        email_label.style.color = 'black';
        email_label.style.top = '0px';
        email_label.style.fontSize = '16px';
    }
});

email_input.addEventListener('focus', function(){
    email_label.style.fontSize = '12px';
    email_label.style.top = '-10px';

});

const controlLabel = (input, label) => {
	if(input.value!=''){
		label.style.top = '-10px';
		label.style.fontSize = '12px';
		label.style.color = '#A0D8B3';
	} if(input.value==''){
		label.style.top = '0px';
		label.style.fontSize = '16px';
		label.style.color = 'black';
	}
}

name_input.addEventListener('focusout', function(){
	controlLabel(name_input, name_label);
});

title_input.addEventListener('focusout', function(){
	controlLabel(title_input, title_label);
});

message_input.addEventListener('focusout', function(){
	controlLabel(message_input, message_label);
});

