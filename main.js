window.addEventListener('load', () => {
	const form = document.querySelector("#Cognizance_Task_1");
	const input = document.querySelector("#Cognizance_Task_2");
	const list_el = document.querySelector("#tasks");

	form.addEventListener('submit', (e) => {
		e.preventDefault();

		const task = input.value;

		const task_el = document.createElement('div');
		task_el.classList.add('task');

		const task_content_el = document.createElement('div');
		task_content_el.classList.add('content');

		task_el.appendChild(task_content_el);

		const xyz = document.createElement('input');
		xyz.classList.add('text');
		xyz.type = 'text';
		xyz.value = task;
		xyz.setAttribute('readonly', 'readonly');

		task_content_el.appendChild(xyz);

		const task_actions_el = document.createElement('div');
		task_actions_el.classList.add('actions');
		
		const task_aman = document.createElement('button');
		task_aman.classList.add('edit');
		task_aman.innerText = 'Edit';

		const task_delete_el = document.createElement('button');
		task_delete_el.classList.add('delete');
		task_delete_el.innerText = 'Delete';

		task_actions_el.appendChild(task_aman);
		task_actions_el.appendChild(task_delete_el);

		task_el.appendChild(task_actions_el);

		list_el.appendChild(task_el);

		input.value = '';

		task_aman.addEventListener('click', (e) => {
			if (task_aman.innerText.toLowerCase() == "edit") {
				task_aman.innerText = "Save";
				xyz.removeAttribute("readonly");
				xyz.focus();
			} else {
				task_aman.innerText = "Edit";
				xyz.setAttribute("readonly", "readonly");
			}
		});

		task_delete_el.addEventListener('click', (e) => {
			list_el.removeChild(task_el);
		});
	});
});