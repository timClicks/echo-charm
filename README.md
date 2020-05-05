# Echo

`echo` charm provides a learning experience for the [Operator Framework][].

Its primary role is to demonstrate how to access config values from within a charm.

To deploy the `echo` charm, clone it from the upstream repository and deploy it as a local charm:

```
git clone https://github.com/timClicks/echo-charm /tmp/echo
cd /tmp/echo
git submodule update --init
juju deploy /tmp/echo
```

Once the charm has been deployed, try changing its config and then see the output of `juju status`.

```
juju config echo message=ping
```

When you next execute `juju status`, you should see "ping" appear in the unit's status line.


Contact
-------
 - Author: Tim McNamara [@timClicks](https://discourse.juju.is/u/timclicks) in the Juju Discourse
 - Report bugs in the [project repository](https://github.com/timClicks/echo-charm/issues) or report them in the Juju Discourse in the #charming category


[Operator Framework]: https://github.com/canonical/operator