import csv
from django.contrib import admin
from django.conf import settings
from django.http import HttpResponse
from django.utils.html import format_html
from django.urls import reverse
from django.contrib.admin.utils import  quote

class CommonAdmin(admin.ModelAdmin):

    #list_per_page = settings.LIST_PER_PAGE
    #list_max_show_all = settings.LIST_PER_PAGE
 

    def __init__(self, model, admin_site):
        self.request = None
        super().__init__(model, admin_site)
    
    def get_action_btn(self,obj):
        pk = obj.id
        edit_url = reverse('admin:%s_%s_change' % (self.opts.app_label,self.opts.model_name),args=(quote(pk),))
        delete_url = reverse('admin:%s_%s_delete' % (self.opts.app_label,self.opts.model_name),args=(quote(pk),))
        history_url = reverse('admin:%s_%s_history' % (self.opts.app_label,self.opts.model_name),args=(quote(pk),))
        html = ''' 
            
                <a href="'''+edit_url+'''" data-toggle="tooltip"  class="btn btn-sm btn-primary" data-original-title="Edit">
                <i class="fas fa-edit"></i> Edit
                </a>
                <a href="'''+delete_url+'''" data-toggle="tooltip" class="btn btn-sm btn-primary" data-original-title="Delete">
                <i class="fas fa-trash-alt"></i> Delete
                </a>
                <a href="'''+history_url+'''" data-toggle="tooltip" class="btn btn-sm btn-primary" data-original-title="History">
                <i class="fas fa-history"></i> History
                </a>
               

            
        '''
        return format_html(html)

    get_action_btn.short_description  = "Actions"

    def get_status(self,obj):
        badge = 'bg-success'
        if obj.status == 0:
            badge = 'bg-warning'
        if obj.status == 1:
            badge = 'bg-success'
        if obj.status == 2:
            badge = 'bg-info'
        if obj.status == 3:
            badge = 'bg-default'
        if obj.status == 4:
            badge = 'bg-success'

        html = '<span class="badge badge-dot mr-4"> <i class="{}"></i>  <span class="status">{}</span>  </span>'
        return format_html(html, badge , obj.get_status_display() )
    get_status.short_description = "Status"

     

    def formfield_for_dbfield(self, db_field, request, **kwargs):
         
        formfield = super().formfield_for_dbfield(db_field, request, **kwargs)
        if hasattr(formfield,'widget'):
            formfield.widget.can_add_related = False
            formfield.widget.can_change_related = False
            formfield.widget.can_delete_related = False
        return formfield

