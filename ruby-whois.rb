require 'rubygems'
require 'whois'
require 'json'

#~ c = Whois::Client.new(:timeout => 20)
#~ r = c.query("google.com")
r = Whois.whois(ARGV[0])

puts JSON.generate({
    'disclaimer' => r.disclaimer,
    'domain' => r.domain,
    'domain_id' => r.domain_id,
    'referral_whois' => r.referral_whois,
    'referral_url' => r.referral_url,
    'status' => r.status,
    'registered?' => r.registered?,
    'available?' => r.available?,
    'created_on' => r.created_on,
    'updated_on' => r.updated_on,
    'expires_on' => r.expires_on,
    'registrar' => r.registrar,
    'registrant_contact' => r.registrant_contact,
    'admin_contact' => r.admin_contact,
    'technical_contact' => r.technical_contact,
    'nameservers' => r.nameservers,
})
