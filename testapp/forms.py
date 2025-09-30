from django import forms
from testapp.models import EmployeeModel

class EmployeeModelForm(forms.ModelForm):
    class Meta:
        model = EmployeeModel
        fields = "__all__"
    def clean_emp_id(self):
        emp_id = self.cleaned_data.get("emp_id")
        if not emp_id or not emp_id.startswith("EMP") or len(emp_id) != 9 or not emp_id[3:].isdigit():
            raise forms.ValidationError('Emp ID must start with EMP followed by 6 digits (e.g. EMP266043)')
        return emp_id
    def clean_emp_sal(self):
        emp_sal = self.cleaned_data.get("emp_sal")
        if emp_sal < 10000 or emp_sal > 800000:
            raise forms.ValidationError('Salary must be between 10,000 and 8,00,000')
        return emp_sal
    def clean_emp_addr(self):
        emp_addr = self.cleaned_data.get("emp_addr")
        if not emp_addr.replace(' ', '').isalpha():
            raise forms.ValidationError('City name should only have letters and spaces')
        return emp_addr
