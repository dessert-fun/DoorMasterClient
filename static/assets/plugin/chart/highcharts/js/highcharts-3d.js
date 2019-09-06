/*
 Highcharts JS v5.0.2 (2016-10-26)

 3D features for Highcharts JS

 @license: www.highcharts.com/license
*/
(function (v) {
    "object" === typeof module && module.exports ? module.exports = v : v(Highcharts)
})(function (v) {
    (function (b) {
        var q = b.deg2rad, l = b.pick;
        b.perspective = function (p, u, y) {
            var e = u.options.chart.options3d, g = y ? u.inverted : !1, h = u.plotWidth / 2, d = u.plotHeight / 2,
                f = e.depth / 2, n = l(e.depth, 1) * l(e.viewDistance, 0), c = u.scale3d || 1,
                a = q * e.beta * (g ? -1 : 1), e = q * e.alpha * (g ? -1 : 1), k = Math.cos(e), t = Math.cos(-a),
                z = Math.sin(e), A = Math.sin(-a);
            y || (h += u.plotLeft, d += u.plotTop);
            return b.map(p, function (a) {
                var b, e;
                e = (g ? a.y : a.x) - h;
                var l = (g ?
                    a.x : a.y) - d, p = (a.z || 0) - f;
                b = t * e - A * p;
                a = -z * A * e + k * l - t * z * p;
                e = k * A * e + z * l + k * t * p;
                l = 0 < n && n < Number.POSITIVE_INFINITY ? n / (e + f + n) : 1;
                b = b * l * c + h;
                a = a * l * c + d;
                return {x: g ? a : b, y: g ? b : a, z: e * c + f}
            })
        }
    })(v);
    (function (b) {
        function q(a) {
            var c = 0, m, b;
            for (m = 0; m < a.length; m++) b = (m + 1) % a.length, c += a[m].x * a[b].y - a[b].x * a[m].y;
            return c / 2
        }

        function l(a) {
            var b = 0, m;
            for (m = 0; m < a.length; m++) b += a[m].z;
            return a.length ? b / a.length : 0
        }

        function p(a, b, m, c, k, d, E, e) {
            var B = [], F = d - k;
            return d > k && d - k > Math.PI / 2 + .0001 ? (B = B.concat(p(a, b, m, c, k, k + Math.PI / 2, E, e)),
                B = B.concat(p(a, b, m, c, k + Math.PI / 2, d, E, e))) : d < k && k - d > Math.PI / 2 + .0001 ? (B = B.concat(p(a, b, m, c, k, k - Math.PI / 2, E, e)), B = B.concat(p(a, b, m, c, k - Math.PI / 2, d, E, e))) : ["C", a + m * Math.cos(k) - m * w * F * Math.sin(k) + E, b + c * Math.sin(k) + c * w * F * Math.cos(k) + e, a + m * Math.cos(d) + m * w * F * Math.sin(d) + E, b + c * Math.sin(d) - c * w * F * Math.cos(d) + e, a + m * Math.cos(d) + E, b + c * Math.sin(d) + e]
        }

        var u = Math.cos, y = Math.PI, e = Math.sin, g = b.animObject, h = b.charts, d = b.color, f = b.defined,
            n = b.deg2rad, c = b.each, a = b.extend, k = b.inArray, t = b.map, z = b.merge, A = b.perspective, v =
                b.pick, D = b.SVGElement, C = b.SVGRenderer, r = b.wrap, w = 4 * (Math.sqrt(2) - 1) / 3 / (y / 2);
        r(C.prototype, "init", function (a) {
            a.apply(this, [].slice.call(arguments, 1));
            c([{name: "darker", slope: .6}, {name: "brighter", slope: 1.4}], function (a) {
                this.definition({
                    tagName: "filter",
                    id: "highcharts-" + a.name,
                    children: [{
                        tagName: "feComponentTransfer",
                        children: [{tagName: "feFuncR", type: "linear", slope: a.slope}, {
                            tagName: "feFuncG",
                            type: "linear",
                            slope: a.slope
                        }, {tagName: "feFuncB", type: "linear", slope: a.slope}]
                    }]
                })
            }, this)
        });
        C.prototype.toLinePath =
            function (a, b) {
                var m = [];
                c(a, function (a) {
                    m.push("L", a.x, a.y)
                });
                a.length && (m[0] = "M", b && m.push("Z"));
                return m
            };
        C.prototype.cuboid = function (a) {
            var c = this.g();
            a = this.cuboidPath(a);
            c.front = this.path(a[0]).attr({"class": "highcharts-3d-front", zIndex: a[3]}).add(c);
            c.top = this.path(a[1]).attr({"class": "highcharts-3d-top", zIndex: a[4]}).add(c);
            c.side = this.path(a[2]).attr({"class": "highcharts-3d-side", zIndex: a[5]}).add(c);
            c.fillSetter = function (a) {
                this.front.attr({fill: a});
                this.top.attr({fill: d(a).brighten(.1).get()});
                this.side.attr({fill: d(a).brighten(-.1).get()});
                this.color = a;
                return this
            };
            c.opacitySetter = function (a) {
                this.front.attr({opacity: a});
                this.top.attr({opacity: a});
                this.side.attr({opacity: a});
                return this
            };
            c.attr = function (a) {
                if (a.shapeArgs || f(a.x)) a = this.renderer.cuboidPath(a.shapeArgs || a), this.front.attr({
                    d: a[0],
                    zIndex: a[3]
                }), this.top.attr({d: a[1], zIndex: a[4]}), this.side.attr({
                    d: a[2],
                    zIndex: a[5]
                }); else return b.SVGElement.prototype.attr.call(this, a);
                return this
            };
            c.animate = function (a, c, b) {
                f(a.x) && f(a.y) ?
                    (a = this.renderer.cuboidPath(a), this.front.attr({zIndex: a[3]}).animate({d: a[0]}, c, b), this.top.attr({zIndex: a[4]}).animate({d: a[1]}, c, b), this.side.attr({zIndex: a[5]}).animate({d: a[2]}, c, b), this.attr({zIndex: -a[6]})) : a.opacity ? (this.front.animate(a, c, b), this.top.animate(a, c, b), this.side.animate(a, c, b)) : D.prototype.animate.call(this, a, c, b);
                return this
            };
            c.destroy = function () {
                this.front.destroy();
                this.top.destroy();
                this.side.destroy();
                return null
            };
            c.attr({zIndex: -a[6]});
            return c
        };
        C.prototype.cuboidPath =
            function (a) {
                function c(a) {
                    return n[a]
                }

                var b = a.x, k = a.y, d = a.z, e = a.height, E = a.width, f = a.depth,
                    n = [{x: b, y: k, z: d}, {x: b + E, y: k, z: d}, {x: b + E, y: k + e, z: d}, {
                        x: b,
                        y: k + e,
                        z: d
                    }, {x: b, y: k + e, z: d + f}, {x: b + E, y: k + e, z: d + f}, {x: b + E, y: k, z: d + f}, {
                        x: b,
                        y: k,
                        z: d + f
                    }], n = A(n, h[this.chartIndex], a.insidePlotArea), d = function (a, b) {
                        var k = [];
                        a = t(a, c);
                        b = t(b, c);
                        0 > q(a) ? k = a : 0 > q(b) && (k = b);
                        return k
                    };
                a = d([3, 2, 1, 0], [7, 6, 5, 4]);
                b = [4, 5, 2, 3];
                k = d([1, 6, 7, 0], b);
                d = d([1, 2, 5, 6], [0, 7, 4, 3]);
                return [this.toLinePath(a, !0), this.toLinePath(k, !0), this.toLinePath(d, !0),
                    l(a), l(k), l(d), 9E9 * l(t(b, c))]
            };
        b.SVGRenderer.prototype.arc3d = function (b) {
            function e(a) {
                var b = !1, c = {}, d;
                for (d in a) -1 !== k(d, h) && (c[d] = a[d], delete a[d], b = !0);
                return b ? c : !1
            }

            var m = this.g(), f = m.renderer, h = "x y r innerR start end".split(" ");
            b = z(b);
            b.alpha *= n;
            b.beta *= n;
            m.top = f.path();
            m.side1 = f.path();
            m.side2 = f.path();
            m.inn = f.path();
            m.out = f.path();
            m.onAdd = function () {
                var a = m.parentGroup, b = m.attr("class");
                m.top.add(m);
                c(["out", "inn", "side1", "side2"], function (c) {
                    m[c].addClass(b + " highcharts-3d-side").add(a)
                })
            };
            m.setPaths = function (a) {
                var b = m.renderer.arc3dPath(a), c = 100 * b.zTop;
                m.attribs = a;
                m.top.attr({d: b.top, zIndex: b.zTop});
                m.inn.attr({d: b.inn, zIndex: b.zInn});
                m.out.attr({d: b.out, zIndex: b.zOut});
                m.side1.attr({d: b.side1, zIndex: b.zSide1});
                m.side2.attr({d: b.side2, zIndex: b.zSide2});
                m.zIndex = c;
                m.attr({zIndex: c});
                a.center && (m.top.setRadialReference(a.center), delete a.center)
            };
            m.setPaths(b);
            m.fillSetter = function (a) {
                var b = d(a).brighten(-.1).get();
                this.fill = a;
                this.side1.attr({fill: b});
                this.side2.attr({fill: b});
                this.inn.attr({fill: b});
                this.out.attr({fill: b});
                this.top.attr({fill: a});
                return this
            };
            c(["opacity", "translateX", "translateY", "visibility"], function (a) {
                m[a + "Setter"] = function (a, b) {
                    m[b] = a;
                    c(["out", "inn", "side1", "side2", "top"], function (c) {
                        m[c].attr(b, a)
                    })
                }
            });
            r(m, "attr", function (b, c, k) {
                var d;
                "object" === typeof c && (d = e(c)) && (a(m.attribs, d), m.setPaths(m.attribs));
                return b.call(this, c, k)
            });
            r(m, "animate", function (a, b, c, k) {
                var d, m = this.attribs, f;
                delete b.center;
                delete b.z;
                delete b.depth;
                delete b.alpha;
                delete b.beta;
                f = g(v(c, this.renderer.globalAnimation));
                f.duration && (b = z(b), d = e(b), b.dummy = 1, d && (f.step = function (a, b) {
                    function c(a) {
                        return m[a] + (v(d[a], m[a]) - m[a]) * b.pos
                    }

                    "dummy" === b.prop && b.elem.setPaths(z(m, {
                        x: c("x"),
                        y: c("y"),
                        r: c("r"),
                        innerR: c("innerR"),
                        start: c("start"),
                        end: c("end")
                    }))
                }), c = f);
                return a.call(this, b, c, k)
            });
            m.destroy = function () {
                this.top.destroy();
                this.out.destroy();
                this.inn.destroy();
                this.side1.destroy();
                this.side2.destroy();
                D.prototype.destroy.call(this)
            };
            m.hide = function () {
                this.top.hide();
                this.out.hide();
                this.inn.hide();
                this.side1.hide();
                this.side2.hide()
            };
            m.show = function () {
                this.top.show();
                this.out.show();
                this.inn.show();
                this.side1.show();
                this.side2.show()
            };
            return m
        };
        C.prototype.arc3dPath = function (a) {
            function b(a) {
                a %= 2 * Math.PI;
                a > Math.PI && (a = 2 * Math.PI - a);
                return a
            }

            var c = a.x, d = a.y, k = a.start, f = a.end - .00001, n = a.r, h = a.innerR, l = a.depth, g = a.alpha,
                t = a.beta, z = Math.cos(k), B = Math.sin(k);
            a = Math.cos(f);
            var q = Math.sin(f), x = n * Math.cos(t), n = n * Math.cos(g), A = h * Math.cos(t), w = h * Math.cos(g),
                h = l * Math.sin(t), r = l * Math.sin(g), l = ["M", c + x * z, d + n * B], l = l.concat(p(c,
                d, x, n, k, f, 0, 0)), l = l.concat(["L", c + A * a, d + w * q]),
                l = l.concat(p(c, d, A, w, f, k, 0, 0)), l = l.concat(["Z"]), C = 0 < t ? Math.PI / 2 : 0,
                t = 0 < g ? 0 : Math.PI / 2, C = k > -C ? k : f > -C ? -C : k,
                v = f < y - t ? f : k < y - t ? y - t : f, D = 2 * y - t, g = ["M", c + x * u(C), d + n * e(C)],
                g = g.concat(p(c, d, x, n, C, v, 0, 0));
            f > D && k < D ? (g = g.concat(["L", c + x * u(v) + h, d + n * e(v) + r]), g = g.concat(p(c, d, x, n, v, D, h, r)), g = g.concat(["L", c + x * u(D), d + n * e(D)]), g = g.concat(p(c, d, x, n, D, f, 0, 0)), g = g.concat(["L", c + x * u(f) + h, d + n * e(f) + r]), g = g.concat(p(c, d, x, n, f, D, h, r)), g = g.concat(["L", c + x * u(D), d + n * e(D)]), g = g.concat(p(c,
                d, x, n, D, v, 0, 0))) : f > y - t && k < y - t && (g = g.concat(["L", c + x * Math.cos(v) + h, d + n * Math.sin(v) + r]), g = g.concat(p(c, d, x, n, v, f, h, r)), g = g.concat(["L", c + x * Math.cos(f), d + n * Math.sin(f)]), g = g.concat(p(c, d, x, n, f, v, 0, 0)));
            g = g.concat(["L", c + x * Math.cos(v) + h, d + n * Math.sin(v) + r]);
            g = g.concat(p(c, d, x, n, v, C, h, r));
            g = g.concat(["Z"]);
            t = ["M", c + A * z, d + w * B];
            t = t.concat(p(c, d, A, w, k, f, 0, 0));
            t = t.concat(["L", c + A * Math.cos(f) + h, d + w * Math.sin(f) + r]);
            t = t.concat(p(c, d, A, w, f, k, h, r));
            t = t.concat(["Z"]);
            z = ["M", c + x * z, d + n * B, "L", c + x * z + h, d + n * B + r, "L", c +
            A * z + h, d + w * B + r, "L", c + A * z, d + w * B, "Z"];
            c = ["M", c + x * a, d + n * q, "L", c + x * a + h, d + n * q + r, "L", c + A * a + h, d + w * q + r, "L", c + A * a, d + w * q, "Z"];
            q = Math.atan2(r, -h);
            d = Math.abs(f + q);
            a = Math.abs(k + q);
            k = Math.abs((k + f) / 2 + q);
            d = b(d);
            a = b(a);
            k = b(k);
            k *= 1E5;
            f = 1E5 * a;
            d *= 1E5;
            return {
                top: l,
                zTop: 1E5 * Math.PI + 1,
                out: g,
                zOut: Math.max(k, f, d),
                inn: t,
                zInn: Math.max(k, f, d),
                side1: z,
                zSide1: .99 * d,
                side2: c,
                zSide2: .99 * f
            }
        }
    })(v);
    (function (b) {
        function q(b, f) {
            var d = b.plotLeft, c = b.plotWidth + d, a = b.plotTop, k = b.plotHeight + a, e = d + b.plotWidth / 2,
                g = a + b.plotHeight / 2, h = Number.MAX_VALUE,
                l = -Number.MAX_VALUE, q = Number.MAX_VALUE, u = -Number.MAX_VALUE, r, w = 1;
            r = [{x: d, y: a, z: 0}, {x: d, y: a, z: f}];
            p([0, 1], function (a) {
                r.push({x: c, y: r[a].y, z: r[a].z})
            });
            p([0, 1, 2, 3], function (a) {
                r.push({x: r[a].x, y: k, z: r[a].z})
            });
            r = y(r, b, !1);
            p(r, function (a) {
                h = Math.min(h, a.x);
                l = Math.max(l, a.x);
                q = Math.min(q, a.y);
                u = Math.max(u, a.y)
            });
            d > h && (w = Math.min(w, 1 - Math.abs((d + e) / (h + e)) % 1));
            c < l && (w = Math.min(w, (c - e) / (l - e)));
            a > q && (w = 0 > q ? Math.min(w, (a + g) / (-q + a + g)) : Math.min(w, 1 - (a + g) / (q + g) % 1));
            k < u && (w = Math.min(w, Math.abs((k - g) / (u - g))));
            return w
        }

        var l = b.Chart, p = b.each, u = b.merge, y = b.perspective, e = b.pick, g = b.wrap;
        l.prototype.is3d = function () {
            return this.options.chart.options3d && this.options.chart.options3d.enabled
        };
        l.prototype.propsRequireDirtyBox.push("chart.options3d");
        l.prototype.propsRequireUpdateSeries.push("chart.options3d");
        b.wrap(b.Chart.prototype, "isInsidePlot", function (b) {
            return this.is3d() || b.apply(this, [].slice.call(arguments, 1))
        });
        var h = b.getOptions();
        u(!0, h, {
            chart: {
                options3d: {
                    enabled: !1, alpha: 0, beta: 0, depth: 100, fitToPlot: !0,
                    viewDistance: 25, frame: {bottom: {size: 1}, side: {size: 1}, back: {size: 1}}
                }
            },
            defs: {style: {textContent: h.defs.style.textContent + "\n.highcharts-3d-top{filter: url(#highcharts-brighter)}\n.highcharts-3d-side{filter: url(#highcharts-darker)}"}}
        });
        g(l.prototype, "setClassName", function (b) {
            b.apply(this, [].slice.call(arguments, 1));
            this.is3d() && (this.container.className += " highcharts-3d-chart")
        });
        b.wrap(b.Chart.prototype, "setChartSize", function (b) {
            var d = this.options.chart.options3d;
            b.apply(this, [].slice.call(arguments,
                1));
            if (this.is3d()) {
                var e = this.inverted, c = this.clipBox, a = this.margin;
                c[e ? "y" : "x"] = -(a[3] || 0);
                c[e ? "x" : "y"] = -(a[0] || 0);
                c[e ? "height" : "width"] = this.chartWidth + (a[3] || 0) + (a[1] || 0);
                c[e ? "width" : "height"] = this.chartHeight + (a[0] || 0) + (a[2] || 0);
                this.scale3d = 1;
                !0 === d.fitToPlot && (this.scale3d = q(this, d.depth))
            }
        });
        g(l.prototype, "redraw", function (b) {
            this.is3d() && (this.isDirtyBox = !0);
            b.apply(this, [].slice.call(arguments, 1))
        });
        g(l.prototype, "renderSeries", function (b) {
            var d = this.series.length;
            if (this.is3d()) for (; d--;) b =
                this.series[d], b.translate(), b.render(); else b.call(this)
        });
        l.prototype.retrieveStacks = function (b) {
            var d = this.series, g = {}, c, a = 1;
            p(this.series, function (k) {
                c = e(k.options.stack, b ? 0 : d.length - 1 - k.index);
                g[c] ? g[c].series.push(k) : (g[c] = {series: [k], position: a}, a++)
            });
            g.totalStacks = a + 1;
            return g
        }
    })(v);
    (function (b) {
        var q, l = b.Axis, p = b.Chart, u = b.each, y = b.extend, e = b.merge, g = b.perspective, h = b.pick,
            d = b.splat, f = b.Tick, n = b.wrap;
        n(l.prototype, "setOptions", function (b, a) {
            b.call(this, a);
            this.chart.is3d() && (b = this.options,
                b.tickWidth = h(b.tickWidth, 0), b.gridLineWidth = h(b.gridLineWidth, 1))
        });
        n(l.prototype, "render", function (b) {
            b.apply(this, [].slice.call(arguments, 1));
            if (this.chart.is3d()) {
                var a = this.chart, c = a.renderer, d = a.options.chart.options3d, f = d.frame, e = f.bottom,
                    g = f.back, f = f.side, h = d.depth, n = this.height, l = this.width, p = this.left, q = this.top;
                this.isZAxis || (this.horiz ? (e = {
                    x: p,
                    y: q + (a.xAxis[0].opposite ? -e.size : n),
                    z: 0,
                    width: l,
                    height: e.size,
                    depth: h,
                    insidePlotArea: !1
                }, this.bottomFrame ? this.bottomFrame.animate(e) : this.bottomFrame =
                    c.cuboid(e).attr({
                        "class": "highcharts-3d-frame highcharts-3d-frame-bottom",
                        zIndex: a.yAxis[0].reversed && 0 < d.alpha ? 4 : -1
                    }).add()) : (d = {
                    x: p + (a.yAxis[0].opposite ? 0 : -f.size),
                    y: q + (a.xAxis[0].opposite ? -e.size : 0),
                    z: h,
                    width: l + f.size,
                    height: n + e.size,
                    depth: g.size,
                    insidePlotArea: !1
                }, this.backFrame ? this.backFrame.animate(d) : this.backFrame = c.cuboid(d).attr({
                    "class": "highcharts-3d-frame highcharts-3d-frame-back",
                    zIndex: -3
                }).add(), a = {
                    x: p + (a.yAxis[0].opposite ? l : -f.size),
                    y: q + (a.xAxis[0].opposite ? -e.size : 0),
                    z: 0,
                    width: f.size,
                    height: n + e.size,
                    depth: h,
                    insidePlotArea: !1
                }, this.sideFrame ? this.sideFrame.animate(a) : this.sideFrame = c.cuboid(a).attr({
                    "class": "highcharts-3d-frame highcharts-3d-frame-side",
                    zIndex: -2
                }).add()))
            }
        });
        n(l.prototype, "getPlotLinePath", function (b) {
            var a = b.apply(this, [].slice.call(arguments, 1));
            if (!this.chart.is3d() || null === a) return a;
            var c = this.chart, d = c.options.chart.options3d, c = this.isZAxis ? c.plotWidth : d.depth,
                d = this.opposite;
            this.horiz && (d = !d);
            a = [this.swapZ({x: a[1], y: a[2], z: d ? c : 0}), this.swapZ({
                x: a[1], y: a[2],
                z: c
            }), this.swapZ({x: a[4], y: a[5], z: c}), this.swapZ({x: a[4], y: a[5], z: d ? 0 : c})];
            a = g(a, this.chart, !1);
            return a = this.chart.renderer.toLinePath(a, !1)
        });
        n(l.prototype, "getLinePath", function (b) {
            return this.chart.is3d() ? [] : b.apply(this, [].slice.call(arguments, 1))
        });
        n(l.prototype, "getPlotBandPath", function (b) {
            if (!this.chart.is3d()) return b.apply(this, [].slice.call(arguments, 1));
            var a = arguments, c = a[1], a = this.getPlotLinePath(a[2]);
            (c = this.getPlotLinePath(c)) && a ? c.push("L", a[10], a[11], "L", a[7], a[8], "L", a[4], a[5],
                "L", a[1], a[2]) : c = null;
            return c
        });
        n(f.prototype, "getMarkPath", function (b) {
            var a = b.apply(this, [].slice.call(arguments, 1));
            if (!this.axis.chart.is3d()) return a;
            a = [this.axis.swapZ({x: a[1], y: a[2], z: 0}), this.axis.swapZ({x: a[4], y: a[5], z: 0})];
            a = g(a, this.axis.chart, !1);
            return a = ["M", a[0].x, a[0].y, "L", a[1].x, a[1].y]
        });
        n(f.prototype, "getLabelPosition", function (b) {
            var a = b.apply(this, [].slice.call(arguments, 1));
            this.axis.chart.is3d() && (a = g([this.axis.swapZ({x: a.x, y: a.y, z: 0})], this.axis.chart, !1)[0]);
            return a
        });
        b.wrap(l.prototype, "getTitlePosition", function (b) {
            var a = this.chart.is3d(), c, d;
            a && (d = this.axisTitleMargin, this.axisTitleMargin = 0);
            c = b.apply(this, [].slice.call(arguments, 1));
            a && (c = g([this.swapZ({
                x: c.x,
                y: c.y,
                z: 0
            })], this.chart, !1)[0], c[this.horiz ? "y" : "x"] += (this.horiz ? 1 : -1) * (this.opposite ? -1 : 1) * d, this.axisTitleMargin = d);
            return c
        });
        n(l.prototype, "drawCrosshair", function (b) {
            var a = arguments;
            this.chart.is3d() && a[2] && (a[2] = {
                plotX: a[2].plotXold || a[2].plotX,
                plotY: a[2].plotYold || a[2].plotY
            });
            b.apply(this, [].slice.call(a,
                1))
        });
        l.prototype.swapZ = function (b, a) {
            if (this.isZAxis) {
                a = a ? 0 : this.chart.plotLeft;
                var c = this.chart;
                return {x: a + (c.yAxis[0].opposite ? b.z : c.xAxis[0].width - b.z), y: b.y, z: b.x - a}
            }
            return b
        };
        q = b.ZAxis = function () {
            this.isZAxis = !0;
            this.init.apply(this, arguments)
        };
        y(q.prototype, l.prototype);
        y(q.prototype, {
            setOptions: function (b) {
                b = e({offset: 0, lineWidth: 0}, b);
                l.prototype.setOptions.call(this, b);
                this.coll = "zAxis"
            }, setAxisSize: function () {
                l.prototype.setAxisSize.call(this);
                this.width = this.len = this.chart.options.chart.options3d.depth;
                this.right = this.chart.chartWidth - this.width - this.left
            }, getSeriesExtremes: function () {
                var b = this, a = b.chart;
                b.hasVisibleSeries = !1;
                b.dataMin = b.dataMax = b.ignoreMinPadding = b.ignoreMaxPadding = null;
                b.buildStacks && b.buildStacks();
                u(b.series, function (c) {
                    if (c.visible || !a.options.chart.ignoreHiddenSeries) b.hasVisibleSeries = !0, c = c.zData, c.length && (b.dataMin = Math.min(h(b.dataMin, c[0]), Math.min.apply(null, c)), b.dataMax = Math.max(h(b.dataMax, c[0]), Math.max.apply(null, c)))
                })
            }
        });
        n(p.prototype, "getAxes", function (b) {
            var a =
                this, c = this.options, c = c.zAxis = d(c.zAxis || {});
            b.call(this);
            a.is3d() && (this.zAxis = [], u(c, function (b, c) {
                b.index = c;
                b.isX = !0;
                (new q(a, b)).setScale()
            }))
        })
    })(v);
    (function (b) {
        function q(b) {
            if (this.chart.is3d()) {
                var d = this.chart.options.plotOptions.column.grouping;
                void 0 === d || d || void 0 === this.group.zIndex || this.zIndexSet || (this.group.attr({zIndex: 10 * this.group.zIndex}), this.zIndexSet = !0)
            }
            b.apply(this, [].slice.call(arguments, 1))
        }

        var l = b.each, p = b.perspective, u = b.pick, y = b.Series, e = b.seriesTypes, g = b.svg;
        b = b.wrap;
        b(e.column.prototype, "translate", function (b) {
            b.apply(this, [].slice.call(arguments, 1));
            if (this.chart.is3d()) {
                var d = this.chart, f = this.options, e = f.depth || 25,
                    c = (f.stacking ? f.stack || 0 : this._i) * (e + (f.groupZPadding || 1));
                !1 !== f.grouping && (c = 0);
                c += f.groupZPadding || 1;
                l(this.data, function (a) {
                    if (null !== a.y) {
                        var b = a.shapeArgs, f = a.tooltipPos;
                        a.shapeType = "cuboid";
                        b.z = c;
                        b.depth = e;
                        b.insidePlotArea = !0;
                        f = p([{x: f[0], y: f[1], z: c}], d, !0)[0];
                        a.tooltipPos = [f.x, f.y]
                    }
                });
                this.z = c
            }
        });
        b(e.column.prototype, "animate", function (b) {
            if (this.chart.is3d()) {
                var d =
                    arguments[1], f = this.yAxis, e = this, c = this.yAxis.reversed;
                g && (d ? l(e.data, function (a) {
                    null !== a.y && (a.height = a.shapeArgs.height, a.shapey = a.shapeArgs.y, a.shapeArgs.height = 1, c || (a.shapeArgs.y = a.stackY ? a.plotY + f.translate(a.stackY) : a.plotY + (a.negative ? -a.height : a.height)))
                }) : (l(e.data, function (a) {
                    null !== a.y && (a.shapeArgs.height = a.height, a.shapeArgs.y = a.shapey, a.graphic && a.graphic.animate(a.shapeArgs, e.options.animation))
                }), this.drawDataLabels(), e.animate = null))
            } else b.apply(this, [].slice.call(arguments, 1))
        });
        b(e.column.prototype, "init", function (b) {
            b.apply(this, [].slice.call(arguments, 1));
            if (this.chart.is3d()) {
                var d = this.options, f = d.grouping, e = d.stacking, c = u(this.yAxis.options.reversedStacks, !0),
                    a = 0;
                if (void 0 === f || f) {
                    f = this.chart.retrieveStacks(e);
                    a = d.stack || 0;
                    for (e = 0; e < f[a].series.length && f[a].series[e] !== this; e++) ;
                    a = 10 * (f.totalStacks - f[a].position) + (c ? e : -e);
                    this.xAxis.reversed || (a = 10 * f.totalStacks - a)
                }
                d.zIndex = a
            }
        });
        b(y.prototype, "alignDataLabel", function (b) {
            if (this.chart.is3d() && ("column" === this.type ||
                "columnrange" === this.type)) {
                var d = arguments[4], e = {x: d.x, y: d.y, z: this.z}, e = p([e], this.chart, !0)[0];
                d.x = e.x;
                d.y = e.y
            }
            b.apply(this, [].slice.call(arguments, 1))
        });
        e.columnrange && b(e.columnrange.prototype, "drawPoints", q);
        b(e.column.prototype, "drawPoints", q)
    })(v);
    (function (b) {
        var q = b.deg2rad, l = b.each, p = b.seriesTypes, u = b.svg;
        b = b.wrap;
        b(p.pie.prototype, "translate", function (b) {
            b.apply(this, [].slice.call(arguments, 1));
            if (this.chart.is3d()) {
                var e = this, g = e.options, h = g.depth || 0, d = e.chart.options.chart.options3d,
                    f = d.alpha, n = d.beta, c = g.stacking ? (g.stack || 0) * h : e._i * h, c = c + h / 2;
                !1 !== g.grouping && (c = 0);
                l(e.data, function (a) {
                    var b = a.shapeArgs;
                    a.shapeType = "arc3d";
                    b.z = c;
                    b.depth = .75 * h;
                    b.alpha = f;
                    b.beta = n;
                    b.center = e.center;
                    b = (b.end + b.start) / 2;
                    a.slicedTranslation = {
                        translateX: Math.round(Math.cos(b) * g.slicedOffset * Math.cos(f * q)),
                        translateY: Math.round(Math.sin(b) * g.slicedOffset * Math.cos(f * q))
                    }
                })
            }
        });
        b(p.pie.prototype.pointClass.prototype, "haloPath", function (b) {
            var e = arguments;
            return this.series.chart.is3d() ? [] : b.call(this,
                e[1])
        });
        b(p.pie.prototype, "drawPoints", function (b) {
            b.apply(this, [].slice.call(arguments, 1));
            this.chart.is3d() && l(this.points, function (b) {
                var e = b.graphic;
                if (e) e[b.y && b.visible ? "show" : "hide"]()
            })
        });
        b(p.pie.prototype, "drawDataLabels", function (b) {
            if (this.chart.is3d()) {
                var e = this.chart.options.chart.options3d;
                l(this.data, function (b) {
                    var g = b.shapeArgs, d = g.r, f = (g.start + g.end) / 2, n = b.labelPos,
                        c = -d * (1 - Math.cos((g.alpha || e.alpha) * q)) * Math.sin(f),
                        a = d * (Math.cos((g.beta || e.beta) * q) - 1) * Math.cos(f);
                    l([0, 2, 4], function (b) {
                        n[b] +=
                            a;
                        n[b + 1] += c
                    })
                })
            }
            b.apply(this, [].slice.call(arguments, 1))
        });
        b(p.pie.prototype, "addPoint", function (b) {
            b.apply(this, [].slice.call(arguments, 1));
            this.chart.is3d() && this.update(this.userOptions, !0)
        });
        b(p.pie.prototype, "animate", function (b) {
            if (this.chart.is3d()) {
                var e = arguments[1], g = this.options.animation, h = this.center, d = this.group, f = this.markerGroup;
                u && (!0 === g && (g = {}), e ? (d.oldtranslateX = d.translateX, d.oldtranslateY = d.translateY, e = {
                    translateX: h[0],
                    translateY: h[1],
                    scaleX: .001,
                    scaleY: .001
                }, d.attr(e), f && (f.attrSetters =
                    d.attrSetters, f.attr(e))) : (e = {
                    translateX: d.oldtranslateX,
                    translateY: d.oldtranslateY,
                    scaleX: 1,
                    scaleY: 1
                }, d.animate(e, g), f && f.animate(e, g), this.animate = null))
            } else b.apply(this, [].slice.call(arguments, 1))
        })
    })(v);
    (function (b) {
        var q = b.perspective, l = b.pick, p = b.seriesTypes;
        b = b.wrap;
        b(p.scatter.prototype, "translate", function (b) {
            b.apply(this, [].slice.call(arguments, 1));
            if (this.chart.is3d()) {
                var p = this.chart, e = l(this.zAxis, p.options.zAxis[0]), g = [], h, d, f;
                for (f = 0; f < this.data.length; f++) h = this.data[f], d = e.isLog &&
                e.val2lin ? e.val2lin(h.z) : h.z, h.plotZ = e.translate(d), h.isInside = h.isInside ? d >= e.min && d <= e.max : !1, g.push({
                    x: h.plotX,
                    y: h.plotY,
                    z: h.plotZ
                });
                p = q(g, p, !0);
                for (f = 0; f < this.data.length; f++) h = this.data[f], e = p[f], h.plotXold = h.plotX, h.plotYold = h.plotY, h.plotZold = h.plotZ, h.plotX = e.x, h.plotY = e.y, h.plotZ = e.z
            }
        });
        b(p.scatter.prototype, "init", function (b, l, e) {
            l.is3d() && (this.axisTypes = ["xAxis", "yAxis", "zAxis"], this.pointArrayMap = ["x", "y", "z"], this.parallelArrays = ["x", "y", "z"], this.directTouch = !0);
            b = b.apply(this, [l, e]);
            this.chart.is3d() && (this.tooltipOptions.pointFormat = this.userOptions.tooltip ? this.userOptions.tooltip.pointFormat || "x: \x3cb\x3e{point.x}\x3c/b\x3e\x3cbr/\x3ey: \x3cb\x3e{point.y}\x3c/b\x3e\x3cbr/\x3ez: \x3cb\x3e{point.z}\x3c/b\x3e\x3cbr/\x3e" : "x: \x3cb\x3e{point.x}\x3c/b\x3e\x3cbr/\x3ey: \x3cb\x3e{point.y}\x3c/b\x3e\x3cbr/\x3ez: \x3cb\x3e{point.z}\x3c/b\x3e\x3cbr/\x3e");
            return b
        })
    })(v)
});
