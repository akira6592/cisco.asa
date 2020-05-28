#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The arg spec for the asa_acls module
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class AclsArgs(object):
    """The arg spec for the asa_acls module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        "config": {
            "elements": "dict",
            "options": {
                "acls": {
                    "elements": "dict",
                    "type": "list",
                    "options": {
                        "name": {"required": True, "type": "str"},
                        "acl_type": {
                            "choices": ["extended", "standard"],
                            "type": "str",
                        },
                        "rename": {"type": "str"},
                        "aces": {
                            "elements": "dict",
                            "type": "list",
                            "options": {
                                "grant": {
                                    "choices": ["permit", "deny"],
                                    "type": "str",
                                },
                                "line": {"type": "int"},
                                "remark": {"type": "str"},
                                "source": {
                                    "type": "dict",
                                    "mutually_exclusive": [
                                        ["address", "any"],
                                        ["wildcard_bits", "any"],
                                    ],
                                    "options": {
                                        "address": {"type": "str"},
                                        "netmask": {"type": "str"},
                                        "any": {"type": "bool"},
                                        "port_protocol": {
                                            "type": "dict",
                                            "options": {
                                                "eq": {"type": "str"},
                                                "gt": {"type": "str"},
                                                "lt": {"type": "str"},
                                                "neq": {"type": "str"},
                                                "range": {
                                                    "type": "dict",
                                                    "options": {
                                                        "start": {
                                                            "type": "int"
                                                        },
                                                        "end": {"type": "int"},
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                                "destination": {
                                    "type": "dict",
                                    "mutually_exclusive": [
                                        ["address", "any"],
                                        ["wildcard_bits", "any"],
                                    ],
                                    "options": {
                                        "address": {"type": "str"},
                                        "netmask": {"type": "str"},
                                        "any": {"type": "bool"},
                                        "port_protocol": {
                                            "type": "dict",
                                            "options": {
                                                "eq": {"type": "str"},
                                                "gt": {"type": "str"},
                                                "lt": {"type": "str"},
                                                "neq": {"type": "str"},
                                                "range": {
                                                    "type": "dict",
                                                    "options": {
                                                        "start": {
                                                            "type": "int"
                                                        },
                                                        "end": {"type": "int"},
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                                "protocol": {"type": "str"},
                                "protocol_options": {
                                    "type": "dict",
                                    "options": {
                                        "protocol_number": {"type": "int"},
                                        "ahp": {"type": "bool"},
                                        "eigrp": {"type": "bool"},
                                        "esp": {"type": "bool"},
                                        "gre": {"type": "bool"},
                                        "icmp": {
                                            "type": "dict",
                                            "options": {
                                                "alternate_address": {
                                                    "type": "bool"
                                                },
                                                "conversion_error": {
                                                    "type": "bool"
                                                },
                                                "echo": {"type": "bool"},
                                                "echo_reply": {"type": "bool"},
                                                "information_reply": {
                                                    "type": "bool"
                                                },
                                                "information_request": {
                                                    "type": "bool"
                                                },
                                                "mask_reply": {"type": "bool"},
                                                "mask_request": {
                                                    "type": "bool"
                                                },
                                                "mobile_redirect": {
                                                    "type": "bool"
                                                },
                                                "parameter_problem": {
                                                    "type": "bool"
                                                },
                                                "redirect": {"type": "bool"},
                                                "router_advertisement": {
                                                    "type": "bool"
                                                },
                                                "router_solicitation": {
                                                    "type": "bool"
                                                },
                                                "source_quench": {
                                                    "type": "bool"
                                                },
                                                "source_route_failed": {
                                                    "type": "bool"
                                                },
                                                "time_exceeded": {
                                                    "type": "bool"
                                                },
                                                "timestamp_reply": {
                                                    "type": "bool"
                                                },
                                                "timestamp_request": {
                                                    "type": "bool"
                                                },
                                                "traceroute": {"type": "bool"},
                                                "unreachable": {
                                                    "type": "bool"
                                                },
                                            },
                                        },
                                        "icmp6": {
                                            "type": "dict",
                                            "options": {
                                                "echo": {"type": "bool"},
                                                "echo_reply": {"type": "bool"},
                                                "membership_query": {
                                                    "type": "bool"
                                                },
                                                "membership_reduction": {
                                                    "type": "bool"
                                                },
                                                "membership_report": {
                                                    "type": "bool"
                                                },
                                                "neighbor_advertisement": {
                                                    "type": "bool"
                                                },
                                                "neighbor_redirect": {
                                                    "type": "bool"
                                                },
                                                "neighbor_solicitation": {
                                                    "type": "bool"
                                                },
                                                "packet_too_big": {
                                                    "type": "bool"
                                                },
                                                "parameter_problem": {
                                                    "type": "bool"
                                                },
                                                "router_advertisement": {
                                                    "type": "bool"
                                                },
                                                "router_renumbering": {
                                                    "type": "bool"
                                                },
                                                "router_solicitation": {
                                                    "type": "bool"
                                                },
                                                "time_exceeded": {
                                                    "type": "bool"
                                                },
                                                "unreachable": {
                                                    "type": "bool"
                                                },
                                            },
                                        },
                                        "igmp": {"type": "bool"},
                                        "igrp": {"type": "bool"},
                                        "ip": {"type": "bool"},
                                        "ipinip": {"type": "bool"},
                                        "ipsec": {"type": "bool"},
                                        "nos": {"type": "bool"},
                                        "ospf": {"type": "bool"},
                                        "pcp": {"type": "bool"},
                                        "pim": {"type": "bool"},
                                        "pptp": {"type": "bool"},
                                        "sctp": {"type": "bool"},
                                        "snp": {"type": "bool"},
                                        "tcp": {"type": "bool"},
                                        "udp": {"type": "bool"},
                                    },
                                },
                                "inactive": {"type": "bool"},
                                "log": {
                                    "type": "str",
                                    "choices": [
                                        "default",
                                        "alerts",
                                        "critical",
                                        "debugging",
                                        "disable",
                                        "emergencies",
                                        "errors",
                                        "informational",
                                        "interval",
                                        "notifications",
                                        "warnings",
                                    ],
                                },
                                "time_range": {"type": "str"},
                            },
                        },
                    },
                }
            },
            "type": "list",
        },
        "running_config": {"type": "str"},
        "state": {
            "choices": [
                "merged",
                "replaced",
                "overridden",
                "deleted",
                "gathered",
                "rendered",
                "parsed",
            ],
            "default": "merged",
            "type": "str",
        },
    }