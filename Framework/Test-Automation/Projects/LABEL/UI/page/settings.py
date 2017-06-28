# coding: utf-8
import Projects.LABEL.pro_config as config


# ******************** LOGIN PAGES ******************** #

# LOGIN PAGE ELEMENTS
AUTH_LOGIN_URL = "%s/auth/login/" % config.BASE_URL
TXT_USER_NAME_ID = "id_username"
TXT_PASSWORD_ID = "id_password"
BTN_LOGIN_XPATH = "//button[@type='submit']"
DIV_CONTAINER_ID = "container"
LABEL_LOGIN_ERROR_XPATH = ".//*[@id='splash']/div[1]/div/div/form/div[1]/fieldset/div[1]/ul/li"

# ******************** COMMON ELEMENTS ******************** #

LABEL_PAGE_ERRORS_XPATH = ".//*[@id='main_content']/div[1]/div"

# ******************** PROJECT PAGES ******************** #

# PROJECT OVERVIEW PAGE ELEMENTS
PROJECT_OVERVIEW_URL = "%s/project" % config.BASE_URL
DIV_OVERVIRE_BOX_ID = "overview-box"
DIV_OVERVIRE_BOX_CONTENT_XPATH = ".//*[@id='overview-box']/div[1]/dl"

# - DIV FOR INSTANCE OVERVIEW
LABEL_INSTANCE_COUNT_XPATH = ".//*[@id='overview-box']/div[1]/dl[1]/dt/a/b"
LABEL_INSTANCE_RATIO_XPATH = ".//*[@id='overview-box']/div[1]/dl[1]/dd[1]/div/span"
LABEL_CORE_RATIO_XPATH = ".//*[@id='overview-box']/div[1]/dl[1]/dd[2]/div/span"
LABEL_RAM_RATIO_XPATH = ".//*[@id='overview-box']/div[1]/dl[1]/dd[3]/div/span"
LABEL_INSTANCE_SNAPSHOT_XPATH = ".//*[@id='overview-box']/div[1]/dl[1]/dd[4]/div/span"

# - DIV FOR VOLUME OVERVIEW
LABEL_VOLUME_COUNT_XPATH = ".//*[@id='overview-box']/div[1]/dl[2]/dt/a/b"
LABEL_VOLUME_RATIO_XPATH = ".//*[@id='overview-box']/div[1]/dl[2]/dd[1]/div/span"
LABEL_SNAPSHOT_RATIO_XPATH = ".//*[@id='overview-box']/div[1]/dl[2]/dd[2]/div/span"
LABEL_GIGABYTES_RATIO_XPATH = ".//*[@id='overview-box']/div[1]/dl[2]/dd[3]/div/span"

# - DIV FOR IMAGE OVERVIEW
LABEL_PUBLIC_IMAGE_COUNT_IN_BOLD_XPATH = ".//*[@id='overview-box']/div[1]/dl[3]/dt/a/b"
LABEL_PUBLIC_IMAGE_COUNT_XPATH = ".//*[@id='overview-box']/div[1]/dl[3]/dd[1]/div/span"
LABEL_LINUX_IMAGE_COUNT_XPATH = ".//*[@id='overview-box']/div[1]/dl[3]/dd[2]/div/span"
LABEL_WINDOWS_IMAGE_COUNT_XPATH = ".//*[@id='overview-box']/div[1]/dl[3]/dd[3]/div/span"
LABEL_ISO_IMAGE_COUNT_XPATH = ".//*[@id='overview-box']/div[1]/dl[3]/dd[4]/div/span"

# - DIV FOR SECURITY GROUP OVERVIEW
LABEL_SECURITY_GROUP_COUNT_XPATH = ".//*[@id='overview-box']/div[1]/dl[4]/dt/a/b"
LABEL_SECURITY_GROUP_RATIO_XPATH = ".//*[@id='overview-box']/div[1]/dl[4]/dd/div/span"

# - DIV FOR NETWORK OVERVIEW
LABEL_NETWORK_COUNT_XPATH = ".//*[@id='overview-box']/div[2]/dl[1]/dt/a/b"
LABEL_NETWORK_RATIO_XPATH = ".//*[@id='overview-box']/div[2]/dl[1]/dd/div/span"

# - DIV FOR FLOATING IP OVERVIEW
LABEL_FLOATING_IP_COUNT_XPATH = ".//*[@id='overview-box']/div[2]/dl[2]/dt/a/b"
LABEL_FLOATING_IP_RATIO_XPATH = ".//*[@id='overview-box']/div[2]/dl[2]/dd/div/span"

# - DIV FOR ROUTER OVERVIEW
LABEL_ROUTER_COUNT_XPATH = ".//*[@id='overview-box']/div[2]/dl[3]/dt/a/b"
LABEL_ROUTER_RATIO_XPATH = ".//*[@id='overview-box']/div[2]/dl[3]/dd/div/span"

# PROJECT INSTANCES PAGE ELEMENTS
PROJECT_INSTANCES_URL = "%s/project/instances/" % config.BASE_URL
UL_INSTANCE_TABS_ID = "instance"
TAB_INSTANCE_XPATH = ".//*[@id='instance']/li[1]/a"
TAB_INSTANCE_SNAPSHOT_XPATH = ".//*[@id='instance']/li[2]/a"
TABLE_INSTANCES_ID = "instances"
BTN_CREATE_INSTANCE_ID = "launch"
BTN_DELETE_INSTANCE_ID = "terminate"
BTN_EDIT_INSTANCE_ID = "edit"
BTN_START_INSTANCE_ID = "start"
BTN_STOP_INSTANCE_ID = "stop"
BTN_ADVANCED_INSTANCE_XPATH = ".//*[@id='instances']/thead/tr[1]/th/div/div[2]/a"
BTN_CREATE_SNAPSHOT_ID = "snapshot"
BTN_MANAGE_IP_ID = "disassociate"
BTN_ATTACH_INTERFACE_ID = "attach_interface"
BTN_DETACH_INTERFACE_ID = "detach_interface"
BTN_PAUSE_INSTANCE_ID = "pause"
BTN_SUSPEND_INSTANCE_ID = "suspend"
BTN_REBOOT_INSTANCE_ID = "reboot"
BTN_REBUILD_INSTANCE_ID = "rebuild"
BTN_RESIZE_INSTANCE_ID = "resize"
BTN_RESET_PASSWORD_ID = "reset_password"
BTN_EDIT_SECGROUPS_ID = "edit_secgroups"
BTN_RESUME_INSTANCE_ID = "resume"
ROW_INSTANCE_XPATH = ".//*[@id='instances']/tbody/tr[@data-display='%s']"
ROW_INSTANCE_BY_ID_XPATH = ".//*[@id='instances']/tbody/tr[@data-object-id='%s']"
TXT_SEARCH_INSTANCE_XPATH = ".//*[@id='instances']/thead/tr[1]/th/div/div[1]/input"
BTN_SEARCH_INSTANCE_ID = "filter"

TABLE_SNAPSHOTS_ID = "images"
BTN_LAUNCH_SNAPSHOT_ID = "table_launch_image"
BTN_DELETE_SNAPSHOT_ID = "delete"
ROW_SNAPSHOT_XPATH = ".//*[@id='images']/tbody/tr[@data-display='%s']"
ROW_SNAPSHOT_BY_ID_XPATH = ".//*[@id='images']/tbody/tr[@data-object-id='%s']"

# - DIALOG FOR INSTANCE CONSOLE
DLG_UL_INSTANCE_DETAILS_ID = "instance_details"
DLG_TAB_IP_ADDRESS_XPATH = ".//*[@id='instance_details']/li[4]/a"
DLG_TABLE_IP_ADDRESS_ID = "instance_details__ipaddress"
DLG_LABELS_NET_NAME_XPATH = ".//*[@id='instance_details__ipaddress']/div/dl/dt"
DLG_LABELS_IP_XPATH = ".//*[@id='instance_details__ipaddress']/div/dl/dd"

DLG_BTN_LOG_GO_XPATH = ".//*[@id='tail_length']/button"
DLG_BTN_LOG_SHOW_ALL_XPATH = ".//*[@id='tail_length']/a"
DLG_TABLE_ACTION_LOG_ID = "audit"
DLG_LIST_ACTION_LOG_XPATH = ".//*[@id='audit']/tbody/tr"
DLG_BTN_CLOSE_XPATH = ".//*[@id='view_wrapper']/a"

# - DIALOG FOR INSTANCE CREATE
FORM_CREATE_INSTANCE_ID = "create_instance_form"
DLG_TXT_VM_NAME_ID = "id_name"
DLG_TAB_SNAPSHOT_XPATH = ".//*[@id='select_images']/div[4]/div/button[2]"
DLG_LIST_IMAGE_XPATH = ".//*[@id='select_images']/div[4]/ul[1]/li"
DLG_LIST_SNAPSHOT_XPATH = ".//*[@id='select_images']/div[4]/ul[2]/li"
DLG_DDL_ZONE_ID = "id_availability_zone"
DLG_DDL_FLAVOR_ID = "id_flavor"
DLG_LIST_SUBNET_XPATH = "//*[@id='configure']/div[7]/ul/li"
DLG_TXT_COUNT_ID = "id_count"
DLG_TXT_VM_USERNAME_ID = "id_username"
DLG_TXT_VM_PWD_ID = "id_password"
DLG_LABEL_CPU_ID = "flavor_vcpus"
DLG_LABEL_MEM_XPATH = ".//*[@id='create_instance_form']/div[1]/table/tbody/tr/td[2]/div[2]/dl/dd[5]/span[2]"
DLG_LABEL_DISK_XPATH = ".//*[@id='create_instance_form']/div[1]/table/tbody/tr/td[2]/div[2]/dl/dd[6]/span[2]"
DLG_LABEL_ERROR_XPATH = ".//*[@id='configure']/div[1]"
DLG_BTN_NEXT_XPATH = ".//*[@id='create_instance_form']/div[2]/div/div[2]/button[1]"
DLG_BTN_CREATE_VM_XPATH = ".//*[@id='create_instance_form']/div[2]/div/div[2]/button[2]"
DLG_BTN_CLOSE_CREATE_XPATH = ".//*[@id='create_instance_modal']/div/div/div/a"
DLG_LABEL_NO_SUBNET_ERROR_ID = "subnetToolTip"
DLG_LABEL_NO_VM_COUNT_XPATH = ".//*[@id='configure']/div[10]"

# - DIALOG FOR INSTANCE EDIT
DLG_TXT_NEW_VM_NAME_ID = "id_name"
DLG_BTN_SAVE_XPATH = ".//*[@id='modal_wrapper']/div/form/div/div/div[3]/input"
DLG_BTN_CANCEL_SAVE_XPATH = ".//*[@id='modal_wrapper']/div/form/div/div/div[3]/a"

# - DIALOG FOR INSTANCE DELETE
DLG_BTN_DELETE_XPATH = ".//*[@id='modal_wrapper']/div/div/div/div[3]/a[1]"
DLG_BTN_CANCEL_DELETE_XPATH = ".//*[@id='modal_wrapper']/div/div/div/div[3]/a[2]"

# - DIALOG FOR INSTANCE STOP
DLG_BTN_STOP_XPATH = ".//*[@id='modal_wrapper']/div/div/div/div[3]/a[1]"
DLG_BTN_CANCEL_STOP_XPATH = ".//*[@id='modal_wrapper']/div/div/div/div[3]/a[2]"

# - DIALOG FOR INSTANCE REBOOT
DLG_BTN_REBOOT_XPATH = ".//*[@id='modal_wrapper']/div/div/div/div[3]/a[1]"
DLG_BIN_CANCEL_REBOOT_XPATH = ".//*[@id='modal_wrapper']/div/div/div/div[3]/a[2]"

# - DIALOG FOR INSTANCE REBUILD
DLG_DDL_IMAGE_ID = "id_image"
DLG_TXT_VM_NEW_PWD_ID = "id_password"
DLG_TXT_VM_CONFIRM_PWD_ID = "id_confirm_password"
DLG_BTN_REBUILD_XPATH = ".//*[@id='rebuild_instance_form']/div[2]/input"
DLG_BIN_CANCEL_REBUILD_XPATH = ".//*[@id='rebuild_instance_form']/div[2]/a"

# - DIALOG FOR INSTANCE RESIZE
DLG_DDL_NEW_FLAVOR_ID = "id_flavor"
DLG_LABEL_NEW_CPU_ID = "flavor_vcpus"
DLG_LABEL_NEW_DISK_ID = "flavor_disk"
DLG_LABEL_NEW_MEM_ID = "flavor_ram"
DLG_BTN_RESIZE_FLAVOR_XPATH = ".//*[@id='modal_wrapper']/div/form/div/div/div[3]/input"
DLG_BTN_CANCEL_RESIZE_FLAVOR_XPATH = ".//*[@id='modal_wrapper']/div/form/div/div/div[3]/a"

# - DIALOG FOR SNAPSHOT CREATE
DLG_TXT_SNAPSHOT_ID = "id_name"
DLG_BTN_CREATE_SNAPSHOT_XPATH = ".//*[@id='create_snapshot_form']/div[2]/input"
DLG_BTN_CANCEL_CREATE_SNAPSHOT_XPATH = ".//*[@id='create_snapshot_form']/div[2]/a"

# - DIALOG FOR SNAPSHOT EDIT
DLG_TXT_NEW_SNNAME_ID = "id_name"
DLG_TXT_NEW_SNDESC_ID = "id_description"
DLG_BTN_EDIT_SNAPSHOT_XPATH = ".//*[@id='modal_wrapper']/div/form/div/div/div[3]/input"
DLG_BTN_CANCEL_EDIT_SNAPSHOT_XATH = ".//*[@id='modal_wrapper']/div/form/div/div/div[3]/a"

# - DIALOG FOR SNAPSHOT DELETE
DLG_BTN_DELETE_SNAPSHOT_XPATH = ".//*[@id='modal_wrapper']/div/div/div/div[3]/a[1]"
DLG_BTN_CANCEL_DELETE_SNAPSHOT_XPATH = ".//*[@id='modal_wrapper']/div/div/div/div[3]/a[2]"

# - DIALOG FOR PUBLIC IP MANAGE
DLG_DLL_SELECT_IP_ID = "select_ip"
DLG_FLOATING_IP_XPATH = ".//*[@id='edit_ips']/tbody/tr/td[3]"
DLG_BTN_UNBIND_IP_XPATH = ".//*[@id='edit_ips']/tbody/tr/td[4]/button"
DLG_BTN_IP_UNBIND_XPATH = ".//*[@id='modal_wrapper']/div[2]/div/div/div[3]/a[1]"
DLG_BTN_IP_CANCEL_UNBIND_XPATH = ".//*[@id='modal_wrapper']/div[2]/div/div/div[3]/a[2]"
DLG_BTN_CLOSE_IP_XPATH = ".//*[@id='router_interface_modal']/div/div/div[3]/a"

# - DIALOG FOR INTERFACE ATTACH
DLG_DDL_NET_ID = "id_network"
DLG_BTN_ATTACH_INTERFACE_XPATH = ".//*[@id='attach_interface_form']/div[2]/input"

# - DIALOG FOR INTERFACE DETACH
DLG_DDL_PORT_ID = "id_port"
DLG_BTN_DETACH_INTERFACE_XPATH = ".//*[@id='detach_interface_form']/div[2]/input"

# - DIALOG FOR PASSWORD RESET
DLG_TXT_NEW_PASSWORD_ID = "id_new_password"
DLG_BTN_RESET_PASSWORD_XPATH = ".//*[@id='reset_password_form']/div[2]/input"
DLG_BIN_CANCEL_RESET_PASSWORD_XPATH = ".//*[@id='reset_password_form']/div[2]/a"

# PROJECT VOLUMES PAGE ELEMENTS
PROJECT_VOLUMES_URL = "%s/project/volumes/" % config.BASE_URL
UL_VOLUMES_AND_SNAPSHOTS_ID = "volumes_and_snapshots"
TAB_VOLUMES_XPATH = ".//*[@id='volumes_and_snapshots']/li[1]/a"
TABLE_VOLUMES_ID = "volumes"
BTN_CREATE_VOLUME_ID = "create"
BTN_EDIT_VOLUME_ID = "edit"
BTN_DELETE_VOLUME_ID = "delete"
BTN_ADVANCED_VOLUME_XPath = ".//*[@id='volumes']/thead/tr[1]/th/div/div[2]/a"
BTN_MANAGE_ATTACHMENT_ID = "attachments"
BTN_EXTEND_VOLUME_ID = "extend"
BTN_CREATE_VOLUME_SNAPSHOT_ID = "table_snapshots"
BTN_CHANGE_VOLUME_TYPE_ID = "retype"
ROW_VOLUMES_XPATH = ".//*[@id='volumes']/tbody/tr[@data-display='%s']"
ROW_VOLUMES_BY_ID_XPATH = ".//*[@id='volumes']/tbody/tr[@data-object-id='%s']"

TAB_VOLUME_SNAPSHOTS_XPATH = ".//*[@id='volumes_and_snapshots']/li[2]/a"
TABLE_VOLUME_SNAPSHOT_ID = "volume_snapshots"
BTN_CREATE_VOLUME_FROM_SNAPSHOTS_ID = "create_from_snapshot"
BTN_EDIT_VOLUME_SNAPSHOT_XPATH = ".//*[@id='volume_snapshots']/thead/tr[1]/th/div/a[2]"
BTN_DELETE_VOLUME_SNAPSHOT_XPATH = ".//*[@id='volume_snapshots']/thead/tr[1]/th/div/button"
ROW_VOLUME_SNAPSHOTS_XPATH = ".//*[@id='volume_snapshots']/tbody/tr[@data-display='%s']"
ROW_VOLUME_SNAPSHOTS_BY_ID_XPATH = ".//*[@id='volume_snapshots']/tbody/tr[@data-object-id='%s']"

# - DIALOG FOR VOLUME DETAILS
DLG_UL_VOLUME_DETAILS_ID = "volume_details"
DLG_LABELS_VOLUME_INFO_XPATH = ".//*[@id='volume_details__overview']/div[1]/dl/dd"
DLG_LABELS_VOLUME_SPECS_XPATH = ".//*[@id='volume_details__overview']/div[2]/dl/dd"
DLG_LABEL_VOLUME_STATUS_XPATH = ".//*[@id='volume_details__overview']/div[3]/dl/dd"

# - DIALOG FOR VOLUME CREATE
DLG_TXT_VOLUME_NAME_ID = "id_name"
DLG_TXT_VOLUME_DESC_ID = "id_description"
DLG_DDL_VOLUME_TYPE_ID = "id_type"
DLG_TXT_VOLUME_SIZE_ID = "id_size"
DLG_DDL_VOLUME_ZONE_ID = "id_availability_zone"
DLG_BTN_CREATE_VOLUME_XPATH = ".//*[@id='create_volume_modal']/div/div/form/div[2]/input"

# - DIALOG FOR VOLUME EDIT
DLG_BTN_EDIT_VOLUME_XPATH = ".//*[@id='update_volume_modal']/div/div/form/div[2]/input"
DLG_BTN_CANCEL_EDIT_VOLUME_XPATH = ".//*[@id='update_volume_modal']/div/div/form/div[2]/a"

# - DIALOG FOR VOLUME DELETE
DLG_BTN_DELETE_VOLUME_XPATH = ".//*[@id='modal_wrapper']/div/div/div/div[3]/a[1]"

# - DIALOG FOR VOLUME EXTEND
DLG_TXT_ORIG_VOLUME_SIZE_ID = "id_orig_size"
DLG_TXT_NEW_VOLUME_SIZE_ID = "id_new_size"
DLG_BTN_EXTEND_VOLUME_XPATH = ".//*[@id='extend_volume_modal']/div/div/form/div[2]/input"
DLG_BTN_CANCEL_EXTEND_VOLUME_XPATH = ".//*[@id='extend_volume_modal']/div/div/form/div[2]/a"

# - DIALOG FOR CHANGE VOLUME TYPE
DLG_SELECT_VOLUME_TYPE_ID = "id_volume_type"
DLG_BTN_CHANGE_VOLUME_TYPE_XPATH = ".//*[@id='retype_volume_modal']/div/div/form/div[2]/input"
DLG_BTN_CANCEL_CHANGE_VOLUME_TYPE_XPATH = ".//*[@id='retype_volume_modal']/div/div/form/div[2]/a"

# - DIALOG FOR ATTACHMENT MANAGE
DLG_TABLE_ATTACHMENTS_ID = "attachments"
DLG_ROW_ATTACHMENT_XPATH = ".//*[@id='attachments']/tbody/tr[@data-object-id='%s']"
DLG_BTN_DETACH_VOLUME_ID = "detach"
DLG_DDL_VM_TO_ATTACH_ID = "id_instance"
DLG_BTN_ATTACH_VOLUME_XPATH = ".//*[@id='attach_volume_form']/div[2]/input"
DLG_BTN_DETACH_VOLUME_XPATH = ".//*[@id='modal_wrapper']/div[2]/div/div/div[3]/a[1]"

# - DIALOG FOR VOLUME SNAPSHOT DETAILS
DLG_UL_VOLUME_SNAPSHOT_DETAILS_ID = "snapshot_details"
DLG_LABELS_VOLUME_SNAPSHOT_INFO_XPATH = ".//*[@id='snapshot_details__overview']/div[1]/dl/dd"
DLG_LABELS_VOLUME_SNAPSHOT_SPECS_XPATH = ".//*[@id='snapshot_details__overview']/div[2]/dl/dd"

# - DIALOG FOR VOLUME SNAPSHOT CREATE
DLG_TXT_SNAPSHOT_NAME_ID = "id_name"
DLG_TXT_SNAPSHOT_DESC_ID = "id_description"
DLG_BTN_CREATE_VOLUME_SANPSHOT_XPATH = ".//*[@id='create_volume_snapshot_modal']/div/div/form/div[2]/input"
DLG_BTN_CANCEL_CREATE_VOLUME_SANPSHOT_XPATH = ".//*[@id='create_volume_snapshot_modal']/div/div/form/div[2]/a"

# - DIALOG FOR VOLUME SNAPSHOT EDIT
DLG_BTN_EDIT_VOLUME_SNAPSHOT_XPATH = ".//*[@id='update_snapshot_form']/div[2]/input"
DLG_BTN_CANCEL_EDIT_VOLUME_SNAPSHOT_XPATH = ".//*[@id='update_snapshot_form']/div[2]/a"

# - DIALOG FOR VOLUME SNAPSHOT DELETE
DLG_BTN_DELETE_VOLUME_SNAPSHOT_XPATH = ".//*[@id='modal_wrapper']/div/div/div/div[3]/a[1]"
DLG_BTN_CANCEL_DELETE_VOLUME_SNAPSHOT_XPATH = ".//*[@id='modal_wrapper']/div/div/div/div[3]/a[2]"

# PROJECT IMAGES PAGE ELEMENTS
PROJECT_IMAGES_URL = "%s/project/images/" % config.BASE_URL
TABLE_IMAGES_ID = "images"
BTN_CREATE_VM_BY_IMAGE_ID = "table_launch_image"
COLUMN_IMAGE_XPATH = ".//*[@id='images']/thead/tr[2]/th[%s]"
LIST_IMAGE_XPATH = ".//*[@id='images']/tbody/tr"
LIST_VISIBLE_IMAGE_XPATH = ".//*[@id='images']/tbody/tr[@style='display: table-row;']"
ROW_IMAGE_XPATH = ".//*[@id='images']/tbody/tr[@data-display='%s']"
ROW_IMAGE_BY_ID_XPATH = ".//*[@id='images']/tbody/tr[@data-object-id='%s']"
BTN_IMAGES_PUBLIC_XPATH = "//*[@id='images']/thead/tr[1]/th/div/div[1]/button[2]"

# - DIALOG FOR IMAGE OVERVIEW
DLG_DIV_IMAGE_DETAILS_ID = "image_details__overview"
DLG_LABELS_IMAGE_INFO_XPATH = ".//*[@id='image_details__overview']/div[1]/dl/dd"
DLG_LABELS_IMAGE_SPECS_XPATH = ".//*[@id='image_details__overview']/div[2]/dl/dd"
DLG_LABELS_IMAGE_PROPERTIES_NAME_XPATH = ".//*[@id='image_details__overview']/div[3]/dl/dt"
DLG_LABELS_IMAGE_PROPERTIES_VALUE_XPATH = ".//*[@id='image_details__overview']/div[3]/dl/dd"

# PROJECT SECURITY GROUP PAGE ELEMENTS
PROJECT_SECURITY_GROUP_URL = "%s/project/access_and_security/" % config.BASE_URL
TABLE_SECURITY_GROUPS_ID = "security_groups"
BTN_CREATE_SECURITY_GROUP_ID = 'create'
BTN_EDIT_SECURITY_GROUP_ID = "edit"
BTN_DELETE_SECURITY_GROUP_ID = 'delete'
LIST_SECURITY_GROUPS_XPATH="//*[@id='security_groups']/tbody/tr"
ROW_SECURITY_GROUP_XPATH = ".//*[@id='security_groups']/tbody/tr[@data-display='%s']"
ROW_SECURITY_GROUP_BY_ID_XPATH = ".//*[@id='security_groups']/tbody/tr[@data-object-id='%s']"
ROW_SECURITY_GROUP_ACTION_XPATH="//*[@id='security_groups']/tbody/tr[@data-display='%s']/td[4]/a"

# - DIALOG FOR SECURITY GROUP CREATE
DLG_TXT_SECURITY_GROUP_NAME_ID = 'id_name'
DLG_TXT_SECURITY_GROUP_DESC_ID = 'id_description'
DLG_BTN_CREATE_SECURITY_GROUP_XPATH = './/*[@id="create_security_group_form"]/div[2]/input'
DLG_BTN_CANCEL_SECURITY_GROUP_XPATH = './/*[@id="create_security_group_form"]/div[2]/a'

# - DIALOG FOR SECURITY GROUP EDIT
DLG_BTN_EDIT_SECURITY_GROUP_XPATH = ".//*[@id='update_security_group_form']/div[2]/input"

# - DIALOG FOR SECURITY GROUP DELETE
DLG_BTN_DELETE_SECURITY_GROUP_XPATH = ".//*[@id='modal_wrapper']/div/div/div/div[3]/a[1]"

# PROJECT SECURITY GROUP RULE PAGE ELEMENTS
TABEL_SECURITY_GROUP_RULES_ID = "rules"
ROW_SECURITY_GROUP_RULE_SELECT_ALL_XPATH = ".//*[@id='rules']/thead/tr[2]/th[1]/div/input"
BTN_SECURITY_GROUP_RULE_DELETE_ID = "delete"
BTN_SECURITY_GROUP_RULE_DELETE_CONFIRM_XPATH = ".//*[@id='modal_wrapper']/div/div/div/div[3]/a[1]"
BTN_SECURITY_GROUP_RULE_ADD_ID = "add_rule"
BTN_SECURITY_GROUP_RULE_TABLE_NEXT_CLASS_NAME = 'table-next'
BTN_SECURITY_GROUP_RULE_TABLE_PREV_CLASS_NAME = 'table-pre'
LIST_SECURITY_GROUP_RULES_XPATH = "//*[@id='rules']/tbody/tr"
ROW_SECURITY_GROUP_RULE_SUB_XPATH = "//*[@id='rules']/tbody/tr/[@data-display=%s]"
DLG_DDL_SECURITY_GROUP_RULES_ID = "id_rule_menu"
DLG_DDL_SECURITY_GROUP_RULE_PORT_ID = "id_port_or_range"
DLG_TXT_SECURITY_GROUP_RULE_PORT_ID = "id_port"
DLG_TXT_SECURITY_GROUP_RULE_ICMP_TYPE_ID = "id_icmp_type"
DLG_TXT_SECURITY_GROUP_RULE_ICMP_CODE_ID = "id_icmp_code"
DLG_TXT_SECURITY_GROUP_RULE_IP_ID = "id_ip_protocol"
DLG_DLL_SECURITY_GROUP_RULE_DIRECTION_ID = "id_direction"
DLG_DLL_SECURITY_GROUP_RULE_DIRECTION_READONLY_ID = "id_direction_readonly"

DLG_DLL_SECURITY_GROUP_RULE_REMOTE_ID = "id_remote"
DLG_TXT_SECURITY_GROUP_RULE_CIDR_ID = "id_cidr"
DLG_DDL_SECURITY_GROUP_RULE_GROUP_ID = "id_security_group"
DLG_DDL_SECURITY_GROUP_RULE_ETHERTYPE_ID = "id_ethertype"
DLG_BTN_SECURITY_GROUP_GROUP_RULE_CANCEL = ".//*[@id='create_security_group_rule_form']/div[2]/a"
DLG_BTN_SECURITY_GROUP_GROUP_RULE_CREATE = ".//*[@id='create_security_group_rule_form']/div[2]/input"

SECURITY_GROUP_SPECIAL_RULE_LIST = ['DNS', 'HTTP', 'HTTPS', 'IMAP', 'IMAPS', 'LDAP', 'MS SQL', 'MYSQL', 'POP3', 'POP3S', 'RDP', 'SMTP', 'SMTPS', 'SSH']

# PROJECT NETWORKS PAGE ELEMENTS
PROJECT_NETWORKS_URL = "%s/project/networks/" % config.BASE_URL
TABLE_NETWORKS_ID = "networks"
BTN_CREATE_NETWORK_ID = "create"
BTN_EDIT_NETWORK_ID = "update"
BTN_DELETE_NETWORK_ID = "delete"
BTN_ADVANCED_NET_XPATH = ".//*[@id='networks']/thead/tr[1]/th/div/div/a"
BTN_MANAGE_SUBNET_ID = "subnet"
ROW_NETWORK_XPATH = ".//*[@id='networks']/tbody/tr[@data-display='%s']"
ROW_NETWORK_BY_ID_XPATH = ".//*[@id='networks']/tbody/tr[@data-object-id='%s']"

# - DIALOG FOR NETWORK CREATE
DLG_TXT_NET_ID = "id_net_name"
DLG_CHB_SUBNET_ID = "id_with_subnet"
DLG_TXT_SUBNET_ID = "id_subnet_name"
DLG_TXT_NET_ADDR_ID = "id_cidr"
DLG_BTN_SHOW_CIDR_XPATH = ".//*[@id='create_network__createnetworkinfoaction']/table/tbody/tr/td[1]/div[4]/div/div/button"
DLG_LIST_CIDR_XPATH = ".//*[@id='create_network__createnetworkinfoaction']/table/tbody/tr/td[1]/div[4]/div/div/ul/li"
DLG_DDL_IP_VERSION_ID = "id_ip_version"
DLG_TXT_GATEWAY_IP_ID = "id_gateway_ip"
DLG_CHB_GATEWAY_ID = "id_no_gateway"
DLG_CHB_DHCP_ID = "id_enable_dhcp"
DLG_TXT_POOLS_ID = "id_allocation_pools"
DLG_TXT_DNS_ID = "id_dns_nameservers"
DLG_BTN_NEXT_NET_XPATH = ".//*[@id='modal_wrapper']/div/form/div/div/div[3]/div/div[2]/button[1]"
DLG_BTN_CREATE_NET_XPATH = ".//*[@id='modal_wrapper']/div/form/div/div/div[3]/div/div[2]/button[2]"

# - DIALOG FOR NETWORK EDIT
DLG_TXT_NET_NAME_ID = "id_name"
DLG_BTN_EDIT_NET_XPATH = ".//*[@id='update_network_form']/div[2]/input"
DLG_BTN_CANCEL_EDIT_NET_XPATH = ".//*[@id='update_network_form']/div[2]/a"

# - DIALOG FOR NETWORK DELETE
DLG_BTN_DELETE_NET_XPATH = ".//*[@id='modal_wrapper']/div/div/div/div[3]/a[1]"
DLG_BTN_CANCEL_DELETE_NET_XPATH = ".//*[@id='modal_wrapper']/div/div/div/div[3]/a[1]"

# - DIALOG FOR SUBNET MANAGE
DLG_TABLE_SUBNETS_ID = "subnets"
DLG_BTN_CREATE_SUBNET_XPATH = ".//*[@id='subnets']/thead/tr[1]/th/div/a"
DLG_BTN_DELETE_SUBNET_XPATH = ".//*[@id='subnets']/thead/tr[1]/th/div/button"
DLG_ROWS_SUBNET_XPATH = ".//*[@id='subnets']/tbody/tr"
DLG_ROW_SUBNET_XPATH = ".//*[@id='subnets']/tbody/tr[@data-display='%s']"
DLG_ROW_SUBNET_BY_ID_XPATH = ".//*[@id='subnets']/tbody/tr[@data-object-id='%s']"
DLG_BTN_DELETE_SUBNET_DELETE_XPATH = ".//*[@id='modal_wrapper']/div[2]/div/div/div[3]/a[1]"
DLG_ROWS_PORT_XPATH = ".//*[@id='ports']/tbody/tr"
DLG_LABEL_PORT_ID = ".//*[@id='update_port_form']/div[1]/div[1]/dl/dd"
DLG_TXT_PORT_NAME_ID = "id_name"
DLG_BTN_EDIT_PORT_SAVE_XPATH = ".//*[@id='update_port_form']/div[2]/input"
DLG_ROW_AGENT_BY_ID_XPATH = ".//*[@id='agents']/tbody/tr[@data-object-id='%s']"
DLG_BTN_ADD_DHCP_AGENT_ID = "add"
DLG_BTN_DELETE_DHCP_AGENT_XPATH = ".//*[@id='agents']/thead/tr[1]/th/div/button"

# - DIALOG FOR SUBNET CREATE
DLG_BTN_ADD_SUBNET_NEXT_XPATH = ".//*[@id='modal_wrapper']/div[2]/form/div/div/div[3]/div/div[2]/button[1]"
DLG_BTN_ADD_SUBNET_CREATE_XPATH = ".//*[@id='modal_wrapper']/div[2]/form/div/div/div[3]/div/div[2]/button[2]"
DLG_BTN_CANCEL_ADD_SUBNET_XPATH = ".//*[@id='modal_wrapper']/div[2]/form/div/div/div[1]/a"

# - DIALOG FOR DHCP AGENT ADD
DLG_DDL_DHCP_AGENT_ID = "id_agent"
DLG_BTN_DHCP_AGENT_ADD_XPATH = ".//*[@id='add_dhcp_agent_form']/div[2]/input"
DLG_BTN_DHCP_AGENT_CANCEL_ADD_XPATH = ".//*[@id='add_dhcp_agent_form']/div[2]/a"

# - DIALOG FOR DHCP AGENT DELETE
DLG_BTN_DHCP_AGENT_DEL_XPATH = ".//*[@id='modal_wrapper']/div[2]/div/div/div[3]/a[1]"
DLG_BTN_DHCP_AGENT_DEL_CANCEL_XPATH = ".//*[@id='modal_wrapper']/div[2]/div/div/div[3]/a[2]"

# - DIALOG FOR SUBNET OVERVIEW
DLG_DIV_SUBNET_DETAILS_ID = "subnet_details__overview"
DLG_LABELS_SUBNET_INFO_XPATH = ".//*[@id='subnet_details__overview']/div/dl/dd"

# PROJECT FLOATING IPS PAGE ELEMENTS
PROJECT_FLOATING_IPS_URL = "%s/project/floating_ips/" % config.BASE_URL
TABLE_FLOATING_IPS_ID = "floating_ips"
BTN_ALLOCATE_FLOATING_IP_ID = "allocate"
BTN_RELEASE_FLOATING_IP_ID = "release"
COLUMN_FLOATING_IP_XPATH = ".//*[@id='floating_ips']/thead/tr[2]/th[%s]"
LIST_FLOATING_IP_XPATH = ".//*[@id='floating_ips']/tbody/tr"
ROW_FLOATING_IP_BY_ID_XPATH = ".//*[@id='floating_ips']/tbody/tr[@data-object-id='%s']"

# - DIALOG FOR FLOATING IP ALLOCATE
DLG_DDL_EXTERNAL_NET_ID = "id_pool"
DLG_BTN_ALLOCATE_IP_XPATH = ".//*[@id='associate_floating_ip_form']/div[2]/input"
DLG_DDL_EXTERNAL_NET_LIST_XPATH = ".//*[@id='id_pool']/option"

# - DIALOG FOR FLOATING IP RELEASE
DLG_BTN_RELEASE_IP_XPATH = ".//*[@id='modal_wrapper']/div/div/div/div[3]/a[1]"
DLG_BTN_CANCEL_RELEASE_IP_XPATH = ".//*[@id='modal_wrapper']/div/div/div/div[3]/a[2]"

# - DIALOG FOR FLOATING IP MAP
DLG_DDL_IP_ID = "id_ip_id"
DLG_DDL_INSTANCE_ID = "id_instance_id"
DLG_BTN_BIND_XPATH = ".//*[@id='modal_wrapper']/div/form/div/div/div[3]/input"

# PROJECT ROUTERS PAGE ELEMENTS
PROJECT_ROUTERS_URL = "%s/project/routers/" % config.BASE_URL
TABLE_ROUTERS_ID = "routers"
BTN_CREATE_ROUTER_ID = "create"
BTN_EDIT_ROUTER_ID = "update"
BTN_DELETE_ROUTER_ID = "delete"
BTN_ADVANCED_ROUTER_XPATH = ".//*[@id='routers']/thead/tr[1]/th/div/div/a"
BTN_SET_GATEWAY_ID = "setgateway"
BTN_CLEAR_GATEWAY_ID = "cleargateway"
BTN_MANAGE_INTERFACE_ID = "table_manage_interface"
COLUMN_ROUTER_XPATH = ".//*[@id='routers']/thead/tr[2]/th[%s]"
LIST_ROUTER_XPATH = ".//*[@id='routers']/tbody/tr"
ROW_ROUTER_XPATH = ".//*[@id='routers']/tbody/tr[@data-display='%s']"
ROW_ROUTER_BY_ID_XPATH = ".//*[@id='routers']/tbody/tr[@data-object-id='%s']"

# - DIALOG FOR ROUTER OVERVIEW
DLG_DIV_ROUTER_DETAILS_ID = "router_details__overview"
DLG_LABELS_ROUTER_INFO_XPATH = ".//*[@id='router_details__overview']/div/dl/dd"

# - DIALOG FOR ROUTER CREATE
DLG_TXT_ROUTER_ID = "id_name"
DLG_DDL_ROUTER_STATE_ID = "id_admin_state"
DLG_CURRENT_ROUTER_STATE_XPATH =".//*[@id ='id_admin_state']/option[@selected='selected']"
DLG_BTN_CREATE_ROUTER_XPATH = ".//*[@id='create_router_modal']/div/div/form/div[2]/input"
DLG_BTN_CANCEL_CREATE_ROUTER_XPATH = ".//*[@id='create_router_modal']/div/div/form/div[2]/a"

# - DIALOG FOR ROUTER EDIT
DLG_BTN_EDIT_ROUTER_XPATH = ".//*[@id='update_router_form']/div[2]/input"
DLG_BTN_CANCEL_EDIT_ROUTER_XPATH = ".//*[@id='update_router_form']/div[2]/a"

# - DIALOG FOR ROUTER DELETE
DLG_BTN_DELETE_ROUTER_XPATH = ".//*[@id='modal_wrapper']/div/div/div/div[3]/a[1]"
DLG_BTN_CANCEL_DELETE_ROUTER_XPATH = ".//*[@id='modal_wrapper']/div/div/div/div[3]/a[2]"

# - DIALOG FOR GATEWAY SET
DLG_DDL_NETWORK_ID = "id_network_id"
DLG_BTN_SET_GATEWAY_XPATH = ".//*[@id='setgateway_form']/div[2]/input"
DLG_BTN_CANCEL_SET_GATEWAY_XPATH = ".//*[@id='setgateway_form']/div[2]/a"

# - DIALOG FOR GATEWAY CLEAR
DLG_BTN_CLEAR_GATEWAY_XPATH = ".//*[@id='modal_wrapper']/div/div/div/div[3]/a[1]"
DLG_BTN_CANCEL_CLEAR_GATEWAY_XPATH = ".//*[@id='modal_wrapper']/div/div/div/div[3]/a[2]"

# - DIALOG FOR INTERFACE MANAGE
DLG_TABLE_INTERFACES_ID = "interfaces"
DLG_BTN_CREATE_INTERFACE_XPATH = ".//*[@id='interfaces']/thead/tr[1]/th/div/a"
DLG_BTN_DELETE_INTERFACE_XPATH = ".//*[@id='interfaces']/thead/tr[1]/th/div/button"
COLUMN_INTERFACE_XPATH = ".//*[@id='interfaces']/thead/tr[2]/th[%s]"
LIST_INTERFACE_XPATH = ".//*[@id='interfaces']/tbody/tr"
ROW_INTERFACE_BY_ID_XPATH = ".//*[@id='interfaces']/tbody/tr[@data-object-id='%s']"

# - DIALOG FOR PORT OVERVIEW
DLG_DIV_PORT_DETAILS_ID = "port_details__overview"
DLG_LABELS_PORT_INFO_XPATH = ".//*[@id='port_details__overview']/div/dl/dd"

# - DIALOG FOR INTERFACE ADD
DLG_DDL_SUBNET_ID = "id_subnet_id"
DLG_TXT_IP_ADDRESS_ID = "id_ip_address"
DLG_BTN_ADD_INTERFACE_XPATH = ".//*[@id='add_interface_form']/div[2]/input"
DLG_BTN_CANCEL_ADD_INTERFACE_XPATH = ".//*[@id='add_interface_form']/div[2]/a"

# - DIALOG FOR INTERFACE DELETE
DLG_BTN_REMOVE_INTERFACE_XPATH = ".//*[@id='modal_wrapper']/div[2]/div/div/div[3]/a[1]"
DLG_BTN_CANCEL_REMOVE_INTERFACE_XPATH = ".//*[@id='modal_wrapper']/div[2]/div/div/div[3]/a[2]"

# PROJECT LOGS PAGE ELEMENTS
PROJECT_LOGS_URL = "%s/project/log/" % config.BASE_URL
TABLE_LOGS_ID = "logs"
LIST_LOGS_XPATH = ".//*[@id='logs']/tbody/tr"
BTN_NEXT_PAGE_XPATH = ".//*[@id='logs']/tfoot/tr/td/div/a[2]"


# ******************** ADMIN PAGES ******************** #

# ADMIN OVERVIEW PAGE ELEMENTS
ADMIN_OVERVIEW_URL = "%s/admin" % config.BASE_URL
UL_OVERVIEW_AND_GRAPH_ID = "overview_and_graph"
TAB_RESOURCE_OVERVIEW_XPATH = ".//*[@id='overview_and_graph']/li[1]/a"
TAB_RESOURCE_DETAILS_XPATH = ".//*[@id='overview_and_graph']/li[2]/a"

# - DIV FOR HYPERVISOR OVERVIEW
LABEL_HYPERVISOR_COUNT_ADMIN_XPATH = ".//*[@id='overview-box']/div[1]/dl[1]/dt/a/b"
LABEL_HYPERVISOR_ACTIVE_ADMIN_XPATH = ".//*[@id='overview-box']/div[1]/dl[1]/dd[1]/div/span"
LABEL_HYPERVISOR_ENABLE_ADMIN_XPATH = ".//*[@id='overview-box']/div[1]/dl[1]/dd[2]/div/span"

# - DIV FOR RESOURCE OVERVIEW
LABEL_RESOURCE_CPU_RATIO_XPATH = ".//*[@id='overview-box']/div[1]/dl[2]/dd[1]/div/span"
LABEL_RESOURCE_MEM_RATIO_XPATH = ".//*[@id='overview-box']/div[1]/dl[2]/dd[2]/div/span"

# - DIV FOR PROJECT OVERVIEW
LABEL_IDENTITY_COUNT_ADMIN_XPATH = ".//*[@id='overview-box']/div[1]/dl[3]/dt/a/b"
LABEL_IDENTITY_RATIO_ADMIN_XPATH = ".//*[@id='overview-box']/div[1]/dl[3]/dd/div/span"

# - DIV FOR USER OVERVIEW
LABEL_IDENTITY_USER_COUNT_ADMIN_XPATH = ".//*[@id='overview-box']/div[1]/dl[4]/dt/a/b"
LABEL_IDENTITY_USER_RATIO_ADMIN_XPATH = ".//*[@id='overview-box']/div[1]/dl[4]/dd/div/span"

# - DIV FOR INSTANCE OVERVIEW
LABEL_INSTANCE_COUNT_IN_BOLD_ADMIN_XPATH = ".//*[@id='overview-box']/div[2]/dl[1]/dt/a/b"
LABEL_INSTANCE_COUNT_ADMIN_XPATH = ".//*[@id='overview-box']/div[2]/dl[1]/dd[1]/div/span"
LABEL_CORE_COUNT_ADMIN_XPATH = ".//*[@id='overview-box']/div[2]/dl[1]/dd[2]/div/span"
LABEL_RAM_SIZE_ADMIN_XPATH = ".//*[@id='overview-box']/div[2]/dl[1]/dd[3]/div/span"
LABEL_INSTANCE_SNAPSHOT_ADMIN_XPATH = ".//*[@id='overview-box']/div[2]/dl[1]/dd[4]/div/span"

# - DIV FOR VOLUME OVERVIEW
LABEL_VOLUME_COUNT_IN_BOLD_ADMIN_XPATH = ".//*[@id='overview-box']/div[2]/dl[2]/dt/a/b"
LABEL_VOLUME_COUNT_ADMIN_XPATH = ".//*[@id='overview-box']/div[2]/dl[2]/dd[1]/div/span"
LABEL_VOLUME_SNAPSHOT_COUNT_ADMIN_XPATH = ".//*[@id='overview-box']/div[2]/dl[2]/dd[2]/div/span"
LABEL_GIGABYTES_SIZE_ADMIN_XPATH = ".//*[@id='overview-box']/div[2]/dl[2]/dd[3]/div/span"

# - DIV FOR IMAGE OVERVIEW
LABEL_IMAGE_COUNT_IN_BOLD_ADMIN_XPATH = ".//*[@id='overview-box']/div[2]/dl[3]/dt/a/b"
LABEL_IMAGE_COUNT_ADMIN_XPATH = ".//*[@id='overview-box']/div[2]/dl[3]/dd[1]/div/span"
LABEL_LINUX_IMAGE_COUNT_ADMIN_XPATH = ".//*[@id='overview-box']/div[2]/dl[3]/dd[2]/div/span"
LABEL_WINDOWS_IMAGE_COUNT_ADMIN_XPATH = ".//*[@id='overview-box']/div[2]/dl[3]/dd[3]/div/span"
LABEL_ISO_IMAGE_COUNT_ADMIN_XPATH = ".//*[@id='overview-box']/div[2]/dl[3]/dd[4]/div/span"

# - DIV FOR SECURITY GROUP OVERVIEW
LABEL_SECURITY_GROUP_COUNT_IN_BOLD_ADMIN_XPATH = ".//*[@id='overview-box']/div[2]/dl[4]/dt/b"
LABEL_SECURITY_GROUP_COUNT_ADMIN_XPATH = ".//*[@id='overview-box']/div[2]/dl[4]/dd/div/span"

# - DIV FOR NETWORK OVERVIEW
LABEL_NETWORK_LINK_XPATH = ".//*[@id='overview-box']/div[3]/dl[1]/dt/a"
LABEL_NETWORK_COUNT_IN_BOLD_ADMIN_XPATH = ".//*[@id='overview-box']/div[3]/dl[1]/dt/a/b"
LABEL_NETWORK_COUNT_ADMIN_XPATH = ".//*[@id='overview-box']/div[3]/dl[1]/dd/div/span"

# - DIV FOR FLOATING IP OVERVIEW
LABEL_FLOATING_IP_COUNT_IN_BOLD_ADMIN_XPATH = ".//*[@id='overview-box']/div[3]/dl[2]/dt/b"
LABEL_FLOATING_IP_COUNT_ADMIN_XPATH = ".//*[@id='overview-box']/div[3]/dl[2]/dd/div/span"

# - DIV FOR ROUTER OVERVIEW
LABEL_ROUTER_COUNT_IN_BOLD_ADMIN_XPATH = ".//*[@id='overview-box']/div[3]/dl[3]/dt/a/b"
LABEL_ROUTER_COUNT_ADMIN_XPATH = ".//*[@id='overview-box']/div[3]/dl[3]/dd/div/span"

# - DIV FOR OVERVIEW DETAILS
TABLE_RESOURCE_DETAILS_ID = "global_usage"
LIST_RESOURCE_DETAILS_XPATH = ".//*[@id='global_usage']/tbody/tr"

# ADMIN AGGREGATES PAGE ELEMENTS
ADMIN_AGGREGATES_URL = "%s/admin/aggregates/" % config.BASE_URL
TABLE_AGGREGATES_ID = "host_aggregates"
BTN_CREATE_AGGREGATE_ID = "create"
BTN_DELETE_AGGREGATE_ID = "delete"
BTN_EDIT_AGGREGATE_ID = "update"
BTN_MANAGE_HYPERVISOR_ID = "manage"
ROW_AGGREGATE_XPATH = ".//*[@id='host_aggregates']/tbody/tr[@data-display='%s']"

# - DIALOG FOR AGGREGATES CREATE
DLG_TXT_AGGREGATES_NAME_ID = "id_name"
DLG_CHB_AGGREGATE_HA_ID = "id_aggregates_HA"
DLG_CHB_OPEN_EVACUATE_ID = "id_open_evacuate"
DLG_TXT_AGGREGATES_ALLOW_NUMBER_ID = "id_number_of_allowable_errors"
DLG_BTN_AGGREGATE_NEXT_XPATH = ".//*[@id='modal_wrapper']/div/form/div/div/div[3]/div/div[2]/button[1]"
DLG_UL_FREE_HOSTS_XPATH = ".//*[@id='available_createaggregatehostsaction']/ul/ul"
DLG_BTN_AGGREGATE_CREATE_XPATH = ".//*[@id='modal_wrapper']/div/form/div/div/div[3]/div/div[2]/button[2]"

# ADMIN INSTANCES PAGE ELEMENTS
ADMIN_INSTANCES_URL = "%s/admin/instances/" % config.BASE_URL
BTN_MIGRATE_INSTANCE_ID = "migrate"

# ADMIN HYPERVISORS PAGE ELEMENTS
ADMIN_HYPERVISORS_URL = "%s/admin/hypervisors/" % config.BASE_URL
TABLE_HYPERVISORS_ID = "hypervisors"
BTN_ENABLE_HYPERVISOR_ID = "enable"
BTN_DISABLE_HYPERVISOR_ID = "disable"
BTN_RATIO_HYPERVISOR_ID = "ratio"
BTN_EVACUATE_HYPERVISOR_ID = "evacuate"
LIST_HYPERVISOR_XPATH = ".//*[@id='hypervisors']/tbody/tr"
ROW_HYPERVISOR_XPATH = ".//*[@id='hypervisors']/tbody/tr[@data-display='%s']"

# - DIALOG FOR HOST OVERVIEW
DLG_UL_HOST_DETAILS_ID = "host_details"
DLG_LABELS_PROCESSOR_INFO_XPATH = ".//*[@id='host_details__overview']/div[1]/dl/dd"
DLG_LABELS_MEMORY_INFO_XPATH = ".//*[@id='host_details__overview']/div[2]/dl/dd"
DLG_LABEL_SHARED_MEMORY_XPATH = ".//*[@id='host_details__overview']/div[3]/dl/dd"
DLG_LABEL_HOST_IP_XPATH = ".//*[@id='host_details__overview']/div[4]/dl/dd"
DLG_LABELS_VM_USAGE_XPATH = ".//*[@id='host_details__overview']/div[5]/div/div[1]/dl/dd"
DLG_LABELS_CPU_USAGE_XPATH = ".//*[@id='host_details__overview']/div[5]/div/div[2]/dl/dd"
DLG_LABELS_MEM_USAGE_XPATH = ".//*[@id='host_details__overview']/div[5]/div/div[3]/dl/dd"
DLG_LABEL_MEN_USED_XPATH = ".//*[@id='host_details__overview']/div[5]/div/div[3]/dl/dd[1]"
DLG_BTN_CLOSE_DIALOG_XPATH = ".//*[@id='view_wrapper']/a"

# ADMIN VOLUMES PAGE ELEMENTS
ADMIN_VOLUMES_URL = "%s/admin/volumes/" % config.BASE_URL
UL_VOLUMES_GROUP_TABS_ID = "volumes_group_tabs"
TAB_ADMIN_VOLUMES_XPATH = ".//*[@id='volumes_group_tabs']/li[1]/a"
TAB_ADMIN_VOLUME_TYPES_XPATH = ".//*[@id='volumes_group_tabs']/li[2]/a"
TAB_ADMIN_VOLUME_SNAPSHOTS_XPATH = ".//*[@id='volumes_group_tabs']/li[3]/a"
TABLE_ADMIN_VOLUME_TYPES_ID = "volume_types"
TABLE_ADMIN_VOLUME_SNAPSHOTS_ID = "volume_snapshots"
BTN_ADMIN_DELETE_VOLUME_TYPE_XPATH = ".//*[@id='volume_types']/thead/tr[1]/th/div/button"
BTN_ADMIN_ADVANCED_VOLUME_XPATH = ".//*[@id='volume_types']/thead/tr[1]/th/div/div/a"
BTN_ADMIN_BIND_QOS_ID = "associate"
BTN_ADMIN_MANAGE_QOS_ID = "manageqos"
ROW_ADMIN_VOLUME_TYPE_XPATH = ".//*[@id='volume_types']/tbody/tr[@data-display='%s']"
ROW_ADMIN_VOLUME_TYPE_BY_ID_XPATH = ".//*[@id='volume_types']/tbody/tr[@data-object-id='%s']"

# - DIALOG FOR VOLUME TYPE CREATE
DLG_TXT_VOLUME_TYPE_NAME_ID = "id_name"
DLG_BTN_CREATE_VOLUME_TYPE_XPATH = ".//*[@id='create_volume_type_modal']/div/div/form/div[2]/input"

# - DIALOG FOR VOLUME TYPE DELETE
DLG_BTN_DELETE_VOLUME_TYPE_XPATH = ".//*[@id='modal_wrapper']/div/div/div/div[3]/a[1]"

# - DIALOG FOR QOS SPECS BIND
DLG_DDL_QOS_SPEC_ID = "id_qos_spec_choice"
DLG_BTN_BIND_QOS_SPEC_XPATH = ".//*[@id='associate_qos_spec_modal']/div/div/form/div[2]/input"
DLG_BTN_MANAGE_QOS_SPEC_XPATH = ".//*[@id='associate_qos_spec_modal']/div/div/form/div[2]/a[1]"
DLG_QOS_SPEC_ID_XPATH = ".//option[contains(text(),'%s')]"

# - DIALOG FOR QOS SPECS MANAGE
DLG_TABLE_QOS_SPECS_ID = "qos_specs"
DLG_BTN_CREATE_QOS_SPEC_XPATH = ".//*[@id='qos_specs']/thead/tr/th/div[1]/a[@id='create']"
DLG_BTN_DELETE_QOS_SPEC_XPATH = ".//*[@id='qos_specs']/thead/tr/th/div[1]/button[@id='delete']"
DLG_BTN_ADVANCED_QOS_SPEC_XPATH = ".//*[@id='qos_specs']/thead/tr[1]/th/div/div/a"
DLG_BTN_MANAGE_QOS_SPEC_ID = "qos_spec"
DLG_ROW_QOS_SPEC_XPATH = ".//*[@id='qos_specs']/tbody/tr[@data-display='%s']"
DLG_ROW_QOS_SPEC_BY_ID_XPATH = ".//*[@id='qos_specs']/tbody/tr[@data-object-id='%s']"
DLG_BTN_CLOSE_QOS_SPEC_XPATH = ".//*[@id='router_interface_modal']/div/div/div[3]/a"

# - DIALOG FOR QOS SPEC CREATE
DLG_TXT_QOS_SPEC_NAME_ID = "id_name"
DLG_BTN_CREATE_OK_QOS_SPEC_XPATH = ".//*[@id='create_volume_type_modal']/div/div/form/div[2]/input"

# - DIALOG FOR QOS SPEC DELETE
DLG_BTN_QOS_SPEC_DELETE_XPATH = ".//*[@id='modal_wrapper']/div[2]/div/div/div[3]/a[1]"
DLG_BTN_QOS_SPEC_CANCEL_DELETE_XPATH = ".//*[@id='modal_wrapper']/div[2]/div/div/div[3]/a[2]"

# - DIALOG FOR QOS SPEC UPDATE
DLG_TXT_QOS_SPEC_OPTION_ID = "id_cidr"
DLG_DDL_QOS_SPEC_OPTION_XPATH = ".//*[@id='modal_wrapper']/div[2]/div/div/form/div[1]/div/div[2]/div[1]/div[1]/div/ul/li"
DLG_BTN_ADD_QOS_SPEC_OPTION_XPATH = ".//*[@id='modal_wrapper']/div[2]/div/div/form/div[1]/div/div[2]/div[1]/div[1]/span/a"
DLG_LIST_QOS_SPEC_OPTIIN_XPATH = ".//*[@id='modal_wrapper']/div[2]/div/div/form/div[1]/div/div[2]/div[1]/div[2]/ul/li"
DLG_BTN_SAVE_QOS_SPEC_XPATH = ".//*[@id='modal_wrapper']/div[2]/div/div/form/div[2]/div/input[1]"

# ADMIN FLAVORS PAGE ELEMENTS
ADMIN_FLAVORS_URL = "%s/admin/flavors/" % config.BASE_URL
TABLE_FLAVORS_ID = "flavors"
BTN_CREATE_FLAVOR_ID = "create"
BTN_DELETE_FLAVOR_ID = "delete"
BTN_UPDATE_FLAVOR_ID = "update"
ROW_FLAVOR_XPATH = ".//*[@id='flavors']/tbody/tr[@data-display='%s']"
ROW_FLAVOR_BY_ID_XPATH = ".//*[@id='flavors']/tbody/tr[@data-object-id='%s']"

# - DIALOG FOR FLAVOR CREATE
DLG_TXT_FLAVOR_NAME_ID = "id_name"
DLG_TXT_FLAVOR_CPU_ID = "id_vcpus"
DLG_TXT_FLAVOR_MEN_ID = "id_memory_mb"
DLG_TXT_FLAVOR_DISK_ID = "id_disk_gb"
DLG_BTN_CREATE_FLAVOR_XPATH = ".//*[@id='modal_wrapper']/div/form/div/div/div[3]/input"

# - DIALOG FOR FLAVOR EDIT
DLG_BTN_SAVE_FLAVOR_XPATH = ".//*[@id='modal_wrapper']/div/form/div/div/div[3]/input"
DLG_BTN_CANCEL_SAVE_FLAVOR_XPATH = ".//*[@id='modal_wrapper']/div/form/div/div/div[3]/a"

# - DIALOG FOR FLAVOR DELETE
DLG_BTN_DELETE_FLAVOR_XPATH = ".//*[@id='modal_wrapper']/div/div/div/div[3]/a[1]"
DLG_BTN_CANCEL_DELETE_FLAVOR_XPATH = ".//*[@id='modal_wrapper']/div/div/div/div[3]/a[2]"

# ADMIN IMAGES PAGE ELEMENTS
ADMIN_IMAGES_URL = "%s/admin/images/" % config.BASE_URL
BTN_ADMIN_CREATE_IMAGE_ID = "create"
BTN_ADMIN_DELETE_IMAGE_ID = "delete"
BTN_ADMIN_EDIT_IMAGE_ID = "edit"
ROW_ADMIN_IMAGE_BY_ID_XPATH = ".//*[@id='images__row__%s']"
BTN_ADMIN_UPDATE_METADATA_XPATH = ".//*[@id='images__row_%s__action_update_metadata']"

# - DIALOG FOR IMAGE CREATE
DLG_TXT_IMAGE_NAME_ID = "id_name"
DLG_TXT_IMAGE_DESC_ID = "id_description"
DLG_BTN_IMAGE_FILE_ID = "id_image_file"
DLG_DDL_IMAGE_FORMAT_ID = "id_disk_format"
DLG_TXT_MIN_DISK_ID = "id_minimum_disk"
DLG_TXT_MIN_MEM_ID = "id_minimum_ram"
DLG_CHB_IS_PUBLIC_ID = "id_is_public"
DLG_CHB_IS_PROTECTED_ID = "id_protected"
DLG_BTN_EDIT_PARAM_XPATH = ".//*[@id='modal_wrapper']/div/form/div/div/div[2]/ul/li[2]/a"
DLG_TXT_IMAGE_BOOTPATH_ID = "bootpath"
DLG_TXT_IMAGE_OS_TYPE_ID = "id_os_type"
DLG_BTN_IMAGE_OS_TYPE_XPATH = ".//*[@id='edit_image__editexpandaction']/table/tbody/tr/td[1]/div[1]/div/div/button"
DLG_BTN_OS_TYPE_XPATH = ".//*[@format-value='%s']"
DLG_DDL_IMAGE_VIF_ID = "id_hw_vif_model"
DLG_TXT_IMAGE_USER_ID = "id_user_name"
DLG_TXT_IMAGE_PASSWORD_ID = "id_pass_word"
DLG_BTN_CREATE_IMAGE_XPATH = ".//*[@id='modal_wrapper']/div/form/div/div/div[3]/input"

# - DIALOG FOR IMAGE EDIT
DLG_CHB_IS_EDIT_PUBLIC_ID = "id_public"
DLG_BTN_EDIT_IMAGE_XPATH = ".//*[@id='modal_wrapper']/div/form/div/div/div[3]/input"
DLG_BTN_CANCEL_EDIT_IMAGE_XPATH = ".//*[@id='modal_wrapper']/div/form/div/div/div[3]/a"

# - DIALOG FOR METADATA UPDATE
DLG_BTN_ADD_METADATA_XPATH = ".//*[@id='modal_wrapper']/div/div/div/form/div[2]/div/input[1]"
DLG_BTN_CANCEL_METADATA_XPATH = ".//*[@id='modal_wrapper']/div/div/div/form/div[2]/div/a"
DLG_TXT_ADD_METADATA_XPATH = ".//*[@id='modal_wrapper']/div/div/div/form/div[1]/div/div[1]/div/div/div/input"
DLG_BTN_ADD_METADATA_TXT_XPATH = ".//*[@id='modal_wrapper']/div/div/div/form/div[1]/div/div[1]/div/div/div/span/a"
DLG_UL_METADATA_XPATH = ".//*[@id='modal_wrapper']/div/div/div/form/div[1]/div/div[2]/div[1]/div/ul/li"
DLG_TXT_METADATA_XPATH = ".//*[@title='%s']/../input"

# - DIALOG FOR IMAGE DELETE
DLG_BTN_DELETE_IMAGE_XPATH = ".//*[@id='modal_wrapper']/div/div/div/div[3]/a[1]"
DLG_BTN_CANCEL_DELETE_IMAGE_XPATH = ".//*[@id='modal_wrapper']/div/div/div/div[3]/a[2]"

# ADMIN NETWORKS PAGE ELEMENTS
ADMIN_NETWORKS_URL = "%s/admin/networks/" % config.BASE_URL

# - DIALOG FOR ADMIN NETWORK CREATE
DLG_TXT_ADMIN_NET_NAME_ID = "id_name"
DLG_DDL_NET_PROJECT_ID = "id_tenant_id"
DLG_TXT_PHYSICAL_NET_ID = "id_physical_network"
DLG_DDL_NET_TYPE_ID = "id_network_type"
DLG_TXT_VLAN_ID_ID = "id_segmentation_id"
DLG_CHB_IS_SHARED_ID = "id_shared"
DLG_CHB_IS_EXT_ID = "id_external"
DLG_BTN_NET_BACK_XPATH = ".//*[@id='modal_wrapper']/div/form/div/div/div[3]/div/div[1]/button"
DLG_BTN_NET_NEXT_XPATH = ".//*[@id='modal_wrapper']/div/form/div/div/div[3]/div/div[2]/button[1]"
DLG_BTN_NET_CREATE_XPATH = ".//*[@id='modal_wrapper']/div/form/div/div/div[3]/div/div[2]/button[2]"

# - DIALOG FOR ADMIN NETWORK EDIT
DLG_BTN_NET_EDIT_XPATH = ".//*[@id='update_network_form']/div[2]/input"
DLG_BTN_NET_CANCEL_EDIT_XPATH = ".//*[@id='update_network_form']/div[2]/a"

# - DIALOG FOR ADMIN NETWORK DELETE
DLG_BTN_NET_DELETE_XPATH = ".//*[@id='modal_wrapper']/div/div/div/div[3]/a[1]"
DLG_BTN_NET_CANCEL_DELETE_XPATH = ".//*[@id='modal_wrapper']/div/div/div/div[3]/a[2]"

# ADMIN ROUTERS PAGE ELEMENTS
ADMIN_ROUTERS_URL = "%s/admin/routers/" % config.BASE_URL
TABLE_ADMIN_ROUTERS_ID = "routers"
BTN_ADMIN_DELETE_ROUTER_ID = "delete"
BTN_ADMIN_EDIT_ROUTER_ID = "update"
BTN_ADMIN_ADVANCED_ROUTER_XPATH = ".//*[@id='routers']/thead/tr[1]/th/div/div/a"
BTN_ADMIN_VIEW_INTERFACE_ID = "table_manage_interface"
ROW_ADMIN_ROUTER_XPATH = ".//*[@id='routers']/tbody/tr[@data-display='%s']"
ROW_ADMIN_ROUTER_BY_ID_XPATH = ".//*[@id='routers']/tbody/tr[@data-object-id='%s']"

# ADMIN DEFAULTS PAGE ELEMENTS
ADMIN_SYSTEM_CONFIG_URL = "%s/admin/system_config/" % config.BASE_URL
TABLE_SYSTEM_CONFIG_ID = "system_config__system_config"
BTN_UPDATE_DEFAULT_ID = "update_defaults"
ROW_DEFAULT_XPATH = ".//*[@id='quotas']/tbody/tr[@data-display='%s']"

# - DIALOG FOR DEFAULT VALUES UPDATE
DLG_TXT_METEDATA_ITEMS_ID = "id_quota-metadata_items"
DLG_TXT_VIRTUAL_CORES_ID = "id_quota-cores"
DLG_TXT_INSTANCE_ID = "id_quota-instances"
DLG_TXT_VOLUMES_ID = "id_quota-volumes"
DLG_TXT_SNAPSHOTS_ID = "id_quota-snapshots"
DLG_TXT_GIGABYTES_ID = "id_quota-gigabytes"
DLG_TXT_MEMORY_ID = "id_quota-ram"
DLG_BTN_UPDATE_DEFAULT_XPATH = ".//*[@id='system_config__system_config']/div[2]/div[1]/form/input[2]"
DLG_BTN_CANCEL_UPDATE_DEFAULT_XPATH = ".//*[@id='modal_wrapper']/div/form/div/div/div[3]/a"

# ADMIN INFO PAGE ELEMENTS
ADMIN_INFO_URL = "%s/admin/info/" % config.BASE_URL
UL_INFO_ID = "system_info"

# ADMIN LOGS PAGE ELEMENTS
ADMIN_LOGS_URL = "%s/admin/log/" % config.BASE_URL


# ******************** IDENTITY PAGES ******************** #

# IDENTITY PROJECTS PAGE ELEMENTS
IDENTITY_PROJECTS_URL = "%s/identity/" % config.BASE_URL
TABLE_PROJECTS_ID = "tenants"
BTN_CREATE_PROJECT_ID = "create"
BTN_EDIT_PROJECT_ID = "update"
BTN_EDIT_QUOTAS_ID = "quotas"
ROW_PROJECT_XPATH = ".//*[@id='tenants']/tbody/tr[@data-display='%s']"
ROW_PROJECT_BY_ID_XPATH = ".//*[@id='tenants']/tbody/tr[@data-object-id='%s']"

# - DIALOG FOR PROJECT CREATE
DLG_TXT_PROJECT_NAME_ID = "id_name"
DLG_TXT_PROJECT_DESC_ID = "id_description"
DLG_CHB_IS_ENABLED_ID = "id_enabled"

DLG_TXT_QUOTA_METEDATA_ITEMS_ID = "id_quota-metadata_items"
DLG_TXT_QUOTA_VIRTUAL_CORES_ID = "id_cores"
DLG_TXT_QUOTA_INSTANCE_ID = "id_instances"
DLG_TXT_QUOTA_VOLUMES_ID = "id_volumes"
DLG_TXT_QUOTA_SNAPSHOTS_ID = "id_snapshots"
DLG_TXT_QUOTA_GIGABYTES_ID = "id_gigabytes"
DLG_TXT_QUOTA_MEMORY_ID = "id_ram"
DLG_TXT_QUOTA_SECURITY_GROUP_ID = "id_security_group"
DLG_TXT_QUOTA_SECURITY_GROUP_RULES_ID = "id_security_group_rule"
DLG_TXT_QUOTA_FLOATING_IP_ID = "id_floatingip"
DLG_TXT_QUOTA_NETWORK_ID = "id_network"
DLG_TXT_QUOTA_ROUTER_ID = "id_router"
DLG_TXT_QUOTA_SUBNET_ID = "id_subnet"

DLG_TAB_MEMBERS_XPATH = ".//*[@id='modal_wrapper']/div/form/div/div/div[2]/ul/li[2]/a"
DLG_TAB_QUOTAS_XPATH = ".//*[@id='modal_wrapper']/div/form/div/div/div[2]/ul/li[3]/a"
DLG_LIST_USERS_TO_ADD_XPATH = ".//*[@id='available_update_members']/ul[1]/ul"
DLG_LIST_PROJECT_MEMBERS_XPATH = ".//*[@id='update_members_members']/ul[1]/ul"
DLG_BTN_SHOW_ROLE_LIST_XPATH = ".//*[@id='update_members_members']/ul[1]/ul/li[3]/a/b"
DLG_BTN_CREATE_PROJECT_NEXT_XPATH = ".//*[@id='modal_wrapper']/div/form/div/div/div[3]/div/div[2]/button[1]"
DLG_BTN_CREATE_PROJECT_XPATH = ".//*[@id='modal_wrapper']/div/form/div/div/div[3]/div/div[2]/button[2]"

# - DIALOG FOR PROJECT QUOTAS EDIT
DLG_TXT_QUOTAS_ERROR_XPATH = ".//*[@id='update_project__update_quotas']/table/tbody/tr/td[1]/div[1]"
DLG_BTN_QUOTAS_CLOSE_XPATH = ".//*[@id='modal_wrapper']/div/form/div/div/div[1]/a"
DLG_BTN_QUOTAS_CANCEL_XPATH = ".//*[@id='modal_wrapper']/div/form/div/div/div[3]/div/div[2]/a"

# IDENTITY USERS PAGE ELEMENTS
IDENTITY_USERS_URL = "%s/identity/users/" % config.BASE_URL
TABLE_USERS_ID = "users"
BTN_CREATE_USER_ID = "create"
BTN_DELETE_USER_ID = "delete"
BTN_EDIT_USER_ID = "edit"
ROW_USER_XPATH = ".//*[@id='users']/tbody/tr[@data-display='%s']"
ROW_USER_BY_ID_XPATH = ".//*[@id='users']/tbody/tr[@data-object-id='%s']"

# - DIALOG FOR USER CREATE
DLG_TXT_USER_ID = "id_name"
DLG_TXT_EMAIL_ID = "id_email"
DLG_TXT_PWD_ID = "id_password"
DLG_TXT_CONFIRM_PWD_ID = "id_confirm_password"
DLG_DDL_PROJECT_ID = "id_project"
DLG_DDL_ROLE_ID = "id_role_id"
DLG_TAB_USER_ROLE_XPATH = ".//*[@id='modal_wrapper']/div/form/div/div/div[2]/ul/li[2]/a"
DLG_CHB_VM_ZONE_SELECTABLE_ID = "id_instance_zone_selectable"
DLG_CHB_VOLUME_ZONE_SELECTABLE_ID = "id_volume_zone_selectable"
DLG_BTN_CREATE_USER_XPATH = ".//input[@type='submit']"

# - DIALOG FOR USER EDIT
DLG_BTN_EDIT_USER_XPATH = ".//*[@id='modal_wrapper']/div/form/div/div/div[3]/input"

# - DIALOG FOR USER DELETE
DLG_BTN_DELETE_USER_XPATH = ".//*[@id='modal_wrapper']/div/div/div/div[3]/a[1]"

# USER CENTER ELEMENTS
MENUS_USER_INFO_XPATH = ".//*[@id='user_info']/div[1]/ul/li"
LABEL_USER_XPATH = ".//*[@id='profile_editor_switcher']/a"
BTN_USER_SETTINGS_XPATH = ".//*[@id='editor_list']/li[1]/a"
BTN_CHANGE_PASSWORD_XPATH = ".//*[@id='editor_list']/li[2]/a"
BTN_LOGOUT_XPATH = ".//*[@id='editor_list']/li[4]/a"

# - DIALOG FOR USER SETTINGS
DLG_TXT_USER_LANGUAGE_ID = "id_language"
DLG_DDL_TIME_ZONE_ID = "id_timezone"
DLG_TXT_PAGE_SIZE_ID = "id_pagesize"
DLG_BTN_SAVE_SETTINGS_XPATH = ".//*[@id='user_settings_modal']/div[2]/button"
DLG_BTN_CANCEL_SAVE_SETTINGS_XPATH = ".//*[@id='user_settings_modal']/div[2]/a"

# - DIALOG FOR PASSWORD CHANGE
DLG_TXT_CURRENT_PASSWORD_ID = "id_current_password"
DLG_TXT_USER_NEW_PASSWORD_ID = "id_new_password"
DLG_TXT_CONFIRM_PASSWORD_ID = "id_confirm_password"
DLG_BTN_MODIFY_PASSWORD_XPATH = ".//*[@id='change_password_modal']/div[2]/button"
DLG_BTN_CANCEL_MODIFY_PASSWORD_XPATH = ".//*[@id='change_password_modal']/div[2]/a"

# PROJECT MENU ELEMENTS
BTN_SELECTED_PROJECT_XPATH = ".//*[@id='container']/div[1]/div[1]/div/button"
LIST_USABLE_PROJECT_XPATH = ".//*[@id='container']/div[1]/div[1]/div/div/div[1]/ul"

# OPERATION TYPE OF LOGS
LOG_DATETIME_FORMAT = "%Y-%m-%d %H:%M"

CONSOLE_LOG_OPERATION_LIST = [ u"登入", u"退出", u"重新配置用户设置", u"修改登入密码", u"创建云主机", u"删除云主机", u"重新配置云主机安全组",
                               u"打开云主机", u"重命名云主机", u"关闭云主机", u"创建快照", u"删除云主机快照", u"重新配置云主机快照",
                               u"云主机绑定接口", u"云主机解绑接口", u"云主机绑定外网IP", u"云主机解绑外网IP", u"分配外网IP", u"释放外网IP",
                               u"挂起云主机", u"重启云主机", u"重建云主机", u"恢复云主机", u"云主机调整配置", u"云主机重置密码", u"创建云硬盘",
                               u"删除云硬盘", u"挂载云硬盘", u"断开挂载云硬盘", u"创建云硬盘快照", u"删除云硬盘快照", u"重新配置云硬盘快照",
                               u"修改云硬盘类型", u"扩展云硬盘", u"重命名云硬盘", u"创建镜像", u"删除镜像", u"重新配置镜像", u"创建安全组",
                               u"重新配置安全组", u"删除安全组", u"添加安全组规则", u"删除安全组规则", u"创建网络", u"重新配置网络", u"删除网络",
                               u"创建子网", u"删除子网", u"重新配置子网", u"创建路由器", u"重新配置路由器", u"删除路由器", u"设置路由网关",
                               u"清除路由网关", u"路由器增加接口", u"路由器删除接口", u"创建弹性策略", u"重新配置弹性策略", u"删除弹性策略",
                               u"弹性扩展", u"创建云主机（弹性策略）", u"弹性收缩", u"删除云主机（弹性策略）", u"导出日志", u"快照上传至镜像",
                               u"创建光盘", u"删除光盘", u"重新配置光盘"]

ISADMIN_LOG_OPERATION_LIST = [ u"登入", u"退出", u"重新配置用户设置", u"修改登入密码", u"创建云主机", u"删除云主机", u"重新配置云主机安全组",
                               u"打开云主机", u"重命名云主机", u"关闭云主机", u"创建快照", u"删除云主机快照", u"重新配置云主机快照",
                               u"云主机绑定接口", u"云主机解绑接口", u"云主机绑定外网IP", u"云主机解绑外网IP", u"分配外网IP", u"释放外网IP",
                               u"挂起云主机", u"重启云主机", u"重建云主机", u"恢复云主机", u"云主机调整配置", u"云主机重置密码", u"云主机冷迁移",
                               u"云主机热迁移", u"创建云主机类型", u"删除云主机类型", u"重新配置云主机类型", u"启用物理主机", u"禁用物理主机",
                               u"疏散云主机", u"疏散", u"重新配置配比", u"移入主机到资源群集", u"从资源群集移除主机", u"创建资源群集", u"删除资源群集",
                               u"重新配置资源群集", u"开启高可用", u"关闭高可用", u"创建云硬盘", u"删除云硬盘", u"挂载云硬盘", u"断开挂载云硬盘",
                               u"创建云硬盘快照", u"删除云硬盘快照", u"重新配置云硬盘快照", u"修改云硬盘类型", u"扩展云硬盘", u"重命名云硬盘",
                               u"创建云硬盘类型", u"删除云硬盘类型", u"关联QoS规格", u"解除QoS规格", u"创建QoS规格", u"删除QoS规格", u"重新配置QoS规格",
                               u"创建镜像", u"删除镜像", u"重新配置镜像", u"创建安全组", u"重新配置安全组", u"删除安全组", u"添加安全组规则",
                               u"删除安全组规则", u"创建网络", u"重新配置网络", u"删除网络", u"创建子网", u"删除子网", u"重新配置子网", u"创建路由器",
                               u"重新配置路由器", u"删除路由器", u"设置路由网关", u"清除路由网关", u"路由器增加接口", u"路由器删除接口", u"创建弹性策略",
                               u"重新配置弹性策略", u"删除弹性策略", u"弹性扩展", u"创建云主机（弹性策略）", u"弹性收缩", u"删除云主机（弹性策略）",
                               u"导出日志", u"创建项目", u"删除项目", u"重新配置项目", u"创建用户", u"删除用户", u"重新配置用户", u"启用用户",u"禁用用户",
                               u"疏散（故障迁移）", u"隔离", u"（故障迁移）", u"更新配额", u"更新日志保留策略日期", u"更新日志保留策略路径", u"快照上传至镜像",
                               u"创建光盘", u"删除光盘", u"重新配置光盘", u"创建外部存储", u"删除外部存储", u"更新外部存储信息"]
