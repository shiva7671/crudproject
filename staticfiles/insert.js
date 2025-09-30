document.getElementById('employeeForm').addEventListener('submit', function(e) {
    let isValid = true;
    const emp_id = document.getElementById('emp_id');
    const empIdError = document.getElementById('empIdError');
    if (!/^EMP\d{6}$/.test(emp_id.value)) {
        empIdError.textContent = 'Emp ID must start with EMP followed by 6 digits (e.g. EMP266043)';
        isValid = false;
    } else {
        empIdError.textContent = '';
    }
    const emp_salary = document.getElementById('emp_salary');
    const empSalaryError = document.getElementById('empSalaryError');
    if (emp_salary.value < 10000 || emp_salary.value > 800000) {
        empSalaryError.textContent = 'Salary must be between 10,000 and 8,00,000';
        isValid = false;
    } else {
        empSalaryError.textContent = '';
    }
    const emp_city = document.getElementById('emp_city');
    const empCityError = document.getElementById('empCityError');
    if (!/^[A-Za-z ]+$/.test(emp_city.value)) {
        empCityError.textContent = 'City name should only have letters and spaces';
        isValid = false;
    } else {
        empCityError.textContent = '';
    }
    const emp_name = document.getElementById('emp_name');
    const empNameError = document.getElementById('empNameError');
    if (emp_name.value.trim() === "") {
        empNameError.textContent = 'Name should not be empty';
        isValid = false;
    } else {
        empNameError.textContent = '';
    }
    if (!isValid) { e.preventDefault(); }
});
