# -*- coding: utf-8 -*-
from odoo import http
import json
from odoo.http import request


class MassMailingExtension(http.Controller):
    @http.route(['/api/v1/c/get_mailing_list_view', '/api/v1/c/get_mailing_list_view/<id>'], type='http', auth='public', methods=['GET'], csrf=False, cors='*')
    def get_mailing_list_view(self, id=None, **params):
        try:
            domain = []
            temp = []
            limit, offset = 0, 0
            if id:
                domain.append(('id', '=', int(id)))
            if "limit" in params and params.get('limit'):
                limit = int(params.get('limit'))
            if "offset" in params and params.get('offset'):
                offset = int(params.get('offset'))

            result = request.env['mailing.list'].sudo().search(domain, limit=limit, offset=offset)
            if result:
                for res in result:
                    dicts = {
                        "id": res.id or False,
                        "name": res.name or "",
                        "is_public": res.is_public or False,
                        "recipients": {
                            'contact_count': res.contact_count or 0.0,
                            'recipients': []
                        },
                        "mailings": {
                            'mailing_count': res.mailing_count or 0.0,
                        },
                        "bounce": {
                            'contact_pct_bounce': res.contact_pct_bounce or 0.0,
                            'bounce': []
                        },
                        "opt_out": {
                            'contact_pct_opt_out': res.contact_pct_opt_out or 0.0,
                            'opt_out': []
                        },
                        "blacklist": {
                            'contact_pct_blacklisted': res.contact_pct_blacklisted or 0.0,
                            'blacklist': []
                        }
                    }
                    for cid in res.contact_ids:
                        vals = {
                            'id': cid.id or False,
                            'create_date': str(cid.create_date) or "",
                            'name': cid.name or "",
                            'email': cid.email or "",
                            'message_bounce': cid.message_bounce or 0.0,
                            'is_blacklisted': cid.is_blacklisted or False,
                            'opt_out': cid.opt_out or False
                        }
                        dicts['recipients']['recipients'].append(vals)
                        if cid.opt_out:
                            dicts['opt_out']['opt_out'].append(vals)
                        if cid.message_bounce:
                            dicts['bounce']['bounce'].append(vals)
                        if cid.is_blacklisted:
                            dicts['blacklist']['blacklist'].append(vals)

                    temp.append(dicts)
                return http.Response(
                    json.dumps({"message": "Success","record": temp, "status": 200}),
                    status=200,
                    mimetype='application/json'
                )
            else:
                return http.Response(
                    json.dumps({"message": "No Data Found.", "status": 200}),
                    status=200,
                    mimetype='application/json'
                )
        except Exception as e:
            return http.Response(
                json.dumps({"message": str(e), "status": 400}),
                status=400,
                mimetype='application/json'
            )
