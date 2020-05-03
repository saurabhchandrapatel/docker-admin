from django.apps import AppConfig


class VirtualizationConfig(AppConfig):
    name = 'virtualization'
    verbose_name = "Virtualization"
    is_navigable = True
    navigation_class = "fas fa-unlock-alt text-orange"
    model_navigation_classes = "ni ni-calendar-grid-58"
    model_navigation_classes_bg_gradient = "bg-gradient-green"
