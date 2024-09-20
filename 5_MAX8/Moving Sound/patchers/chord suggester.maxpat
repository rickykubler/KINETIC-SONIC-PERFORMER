{
	"patcher" : 	{
		"fileversion" : 1,
		"appversion" : 		{
			"major" : 8,
			"minor" : 5,
			"revision" : 5,
			"architecture" : "x64",
			"modernui" : 1
		}
,
		"classnamespace" : "box",
		"rect" : [ 69.0, 62.0, 914.0, 596.0 ],
		"bglocked" : 0,
		"openinpresentation" : 1,
		"default_fontsize" : 12.0,
		"default_fontface" : 0,
		"default_fontname" : "Arial",
		"gridonopen" : 1,
		"gridsize" : [ 15.0, 15.0 ],
		"gridsnaponopen" : 1,
		"objectsnaponopen" : 1,
		"statusbarvisible" : 2,
		"toolbarvisible" : 1,
		"lefttoolbarpinned" : 0,
		"toptoolbarpinned" : 0,
		"righttoolbarpinned" : 0,
		"bottomtoolbarpinned" : 0,
		"toolbars_unpinned_last_save" : 0,
		"tallnewobj" : 0,
		"boxanimatetime" : 200,
		"enablehscroll" : 1,
		"enablevscroll" : 1,
		"devicewidth" : 0.0,
		"description" : "",
		"digest" : "",
		"tags" : "",
		"style" : "",
		"subpatcher_template" : "",
		"assistshowspatchername" : 0,
		"boxes" : [ 			{
				"box" : 				{
					"id" : "obj-50",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"patching_rect" : [ 122.5, 5.0, 100.0, 22.0 ],
					"text" : "loadbang"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-48",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "bang", "bang" ],
					"patching_rect" : [ 122.5, 29.0, 43.0, 22.0 ],
					"text" : "t b b"
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.986246049404144, 0.007120788097382, 0.027434188872576, 1.0 ],
					"bgcolor2" : [ 0.986042201519012, 0.008206307888031, 0.501919090747833, 1.0 ],
					"bgfillcolor_angle" : 270.0,
					"bgfillcolor_autogradient" : 0.0,
					"bgfillcolor_color" : [ 0.986042201519012, 0.008206307888031, 0.501919090747833, 1.0 ],
					"bgfillcolor_color1" : [ 0.986246049404144, 0.007120788097382, 0.027434188872576, 1.0 ],
					"bgfillcolor_color2" : [ 0.986042201519012, 0.008206307888031, 0.501919090747833, 1.0 ],
					"bgfillcolor_proportion" : 0.39,
					"bgfillcolor_type" : "gradient",
					"fontface" : 1,
					"fontsize" : 20.0,
					"gradient" : 1,
					"id" : "obj-27",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 237.0, 590.0, 210.0, 31.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 133.0, 4.5, 192.0, 31.0 ],
					"style" : "redness",
					"text" : "MARKOV MODEL",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-73",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 659.0, 303.0, 100.0, 22.0 ],
					"text" : "loadmess 4"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-71",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1098.0, 389.5, 84.0, 20.0 ],
					"presentation" : 1,
					"presentation_linecount" : 2,
					"presentation_rect" : [ 390.0, 189.5, 53.0, 33.0 ],
					"text" : "MIDI CHORD"
				}

			}
, 			{
				"box" : 				{
					"comment" : "",
					"id" : "obj-65",
					"index" : 3,
					"maxclass" : "outlet",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1066.0, 431.0, 30.0, 30.0 ]
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.986246049404144, 0.007120788097382, 0.027434188872576, 1.0 ],
					"bgcolor2" : [ 0.986042201519012, 0.008206307888031, 0.501919090747833, 1.0 ],
					"bgfillcolor_angle" : 270.0,
					"bgfillcolor_autogradient" : 0.0,
					"bgfillcolor_color" : [ 0.986042201519012, 0.008206307888031, 0.501919090747833, 1.0 ],
					"bgfillcolor_color1" : [ 0.986246049404144, 0.007120788097382, 0.027434188872576, 1.0 ],
					"bgfillcolor_color2" : [ 0.986042201519012, 0.008206307888031, 0.501919090747833, 1.0 ],
					"bgfillcolor_proportion" : 0.39,
					"bgfillcolor_type" : "gradient",
					"fontface" : 1,
					"fontsize" : 20.0,
					"gradient" : 1,
					"id" : "obj-66",
					"linecount" : 2,
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 1109.0, 431.0, 73.0, 53.0 ],
					"presentation" : 1,
					"presentation_linecount" : 2,
					"presentation_rect" : [ 315.0, 180.5, 73.0, 53.0 ],
					"style" : "redness",
					"text" : "53 56 60",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 1.0, 0.788235, 0.470588, 1.0 ],
					"bgoncolor" : [ 0.55, 0.55, 0.55, 1.0 ],
					"fontface" : 1,
					"hint" : "",
					"id" : "obj-1",
					"ignoreclick" : 1,
					"legacytextcolor" : 1,
					"maxclass" : "textbutton",
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "", "", "int" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 29.5, 44.5, 29.0, 27.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 7.0, 131.0, 29.0, 27.0 ],
					"rounded" : 60.0,
					"text" : "2",
					"textcolor" : [ 0.34902, 0.34902, 0.34902, 1.0 ],
					"textoncolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"textovercolor" : [ 0.2, 0.2, 0.2, 1.0 ],
					"usebgoncolor" : 1,
					"usetextovercolor" : 1
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 1.0, 0.788235294117647, 0.470588235294118, 1.0 ],
					"bgoncolor" : [ 0.55, 0.55, 0.55, 1.0 ],
					"fontface" : 1,
					"hint" : "",
					"id" : "obj-20",
					"ignoreclick" : 1,
					"legacytextcolor" : 1,
					"maxclass" : "textbutton",
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "", "", "int" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 208.0, 48.5, 29.0, 27.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 7.0, 43.5, 29.0, 27.0 ],
					"rounded" : 60.0,
					"text" : "1",
					"textcolor" : [ 0.34902, 0.34902, 0.34902, 1.0 ],
					"textoncolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"textovercolor" : [ 0.2, 0.2, 0.2, 1.0 ],
					"usebgoncolor" : 1,
					"usetextovercolor" : 1
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 1.0, 0.788235, 0.470588, 1.0 ],
					"bgoncolor" : [ 0.55, 0.55, 0.55, 1.0 ],
					"fontface" : 1,
					"hint" : "",
					"id" : "obj-2",
					"ignoreclick" : 1,
					"legacytextcolor" : 1,
					"maxclass" : "textbutton",
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "", "", "int" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 33.0, 344.0, 29.0, 27.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 230.0, 131.0, 29.0, 27.0 ],
					"rounded" : 60.0,
					"text" : "3",
					"textcolor" : [ 0.34902, 0.34902, 0.34902, 1.0 ],
					"textoncolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"textovercolor" : [ 0.2, 0.2, 0.2, 1.0 ],
					"usebgoncolor" : 1,
					"usetextovercolor" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-8",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 937.0, 322.0, 126.0, 20.0 ],
					"presentation" : 1,
					"presentation_linecount" : 3,
					"presentation_rect" : [ 247.0, 180.5, 59.0, 47.0 ],
					"text" : "MIDI CHORD NORM"
				}

			}
, 			{
				"box" : 				{
					"comment" : "",
					"id" : "obj-42",
					"index" : 2,
					"maxclass" : "outlet",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 885.150000000000091, 304.0, 30.0, 30.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-61",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 250.0, 52.0, 105.0, 20.0 ],
					"presentation" : 1,
					"presentation_linecount" : 2,
					"presentation_rect" : [ 230.0, 76.5, 64.0, 33.0 ],
					"text" : "open DATASET"
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.176470588235294, 0.215686274509804, 1.0, 1.0 ],
					"bgcolor2" : [ 0.2, 0.2, 0.2, 1.0 ],
					"bgfillcolor_angle" : 270.0,
					"bgfillcolor_autogradient" : 0.0,
					"bgfillcolor_color" : [ 0.176470588235294, 0.215686274509804, 1.0, 1.0 ],
					"bgfillcolor_color1" : [ 0.176470588235294, 0.215686274509804, 1.0, 1.0 ],
					"bgfillcolor_color2" : [ 0.2, 0.2, 0.2, 1.0 ],
					"bgfillcolor_proportion" : 0.5,
					"bgfillcolor_type" : "gradient",
					"fontsize" : 20.0,
					"gradient" : 1,
					"id" : "obj-59",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 295.0, 79.0, 76.0, 31.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 230.0, 43.5, 76.0, 31.0 ],
					"text" : "open",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"fontsize" : 8.0,
					"id" : "obj-55",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 295.0, 188.0, 70.0, 17.0 ],
					"text" : "loadmess 2"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-49",
					"linecount" : 2,
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 349.0, 204.5, 54.0, 33.0 ],
					"presentation" : 1,
					"presentation_linecount" : 2,
					"presentation_rect" : [ 99.0, 38.0, 54.0, 33.0 ],
					"text" : "choose order"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-46",
					"maxclass" : "number",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 295.0, 215.5, 50.0, 22.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 47.0, 43.5, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-43",
					"linecount" : 2,
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 295.0, 244.0, 50.0, 35.0 ],
					"text" : "order $1"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-39",
					"linecount" : 2,
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 73.0, 383.0, 105.0, 33.0 ],
					"presentation" : 1,
					"presentation_linecount" : 2,
					"presentation_rect" : [ 303.0, 131.0, 105.0, 33.0 ],
					"text" : "generate NEW chord"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-33",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 180.0, 165.0, 105.0, 20.0 ],
					"presentation" : 1,
					"presentation_linecount" : 2,
					"presentation_rect" : [ 334.0, 76.5, 64.0, 33.0 ],
					"text" : "reset MODEL"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-26",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 323.5, 119.0, 105.0, 20.0 ],
					"presentation" : 1,
					"presentation_linecount" : 2,
					"presentation_rect" : [ 125.0, 78.5, 65.0, 33.0 ],
					"text" : "load DATASET"
				}

			}
, 			{
				"box" : 				{
					"comment" : "",
					"id" : "obj-23",
					"index" : 1,
					"maxclass" : "outlet",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 53.0, 484.0, 30.0, 30.0 ]
				}

			}
, 			{
				"box" : 				{
					"comment" : "",
					"id" : "obj-3",
					"index" : 1,
					"maxclass" : "inlet",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"patching_rect" : [ 73.0, 326.0, 30.0, 30.0 ]
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.986246049404144, 0.007120788097382, 0.027434188872576, 1.0 ],
					"bgcolor2" : [ 0.986042201519012, 0.008206307888031, 0.501919090747833, 1.0 ],
					"bgfillcolor_angle" : 270.0,
					"bgfillcolor_autogradient" : 0.0,
					"bgfillcolor_color" : [ 0.986042201519012, 0.008206307888031, 0.501919090747833, 1.0 ],
					"bgfillcolor_color1" : [ 0.986246049404144, 0.007120788097382, 0.027434188872576, 1.0 ],
					"bgfillcolor_color2" : [ 0.986042201519012, 0.008206307888031, 0.501919090747833, 1.0 ],
					"bgfillcolor_proportion" : 0.39,
					"bgfillcolor_type" : "gradient",
					"fontface" : 1,
					"fontsize" : 20.0,
					"gradient" : 1,
					"id" : "obj-68",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 931.0, 287.0, 73.0, 31.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 173.0, 180.5, 73.0, 31.0 ],
					"style" : "redness",
					"text" : "0 3 7",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-101",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 447.0, 227.5, 104.0, 20.0 ],
					"presentation" : 1,
					"presentation_linecount" : 2,
					"presentation_rect" : [ 84.0, 190.5, 59.0, 33.0 ],
					"text" : "ACTUAL CHORD"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-90",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 6,
					"outlettype" : [ "signal", "bang", "int", "float", "", "list" ],
					"patching_rect" : [ 746.75, 171.5, 100.0, 22.0 ],
					"text" : "typeroute~"
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.986246049404144, 0.007120788097382, 0.027434188872576, 1.0 ],
					"bgcolor2" : [ 0.986042201519012, 0.008206307888031, 0.501919090747833, 1.0 ],
					"bgfillcolor_angle" : 270.0,
					"bgfillcolor_autogradient" : 0.0,
					"bgfillcolor_color" : [ 0.986042201519012, 0.008206307888031, 0.501919090747833, 1.0 ],
					"bgfillcolor_color1" : [ 0.986246049404144, 0.007120788097382, 0.027434188872576, 1.0 ],
					"bgfillcolor_color2" : [ 0.986042201519012, 0.008206307888031, 0.501919090747833, 1.0 ],
					"bgfillcolor_proportion" : 0.39,
					"bgfillcolor_type" : "gradient",
					"fontface" : 1,
					"fontsize" : 20.0,
					"gradient" : 1,
					"id" : "obj-51",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 455.0, 194.5, 73.0, 31.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 6.0, 190.5, 73.0, 31.0 ],
					"style" : "redness",
					"text" : "Fm",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-41",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "int" ],
					"patching_rect" : [ 717.75, 548.0, 35.0, 22.0 ],
					"text" : "* 2"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-38",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"patching_rect" : [ 608.0, 444.0, 100.0, 22.0 ],
					"text" : "t l l"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-37",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"patching_rect" : [ 717.75, 521.0, 43.200000000000045, 22.0 ],
					"text" : "zl.len"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-35",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 650.0, 532.0, 50.0, 22.0 ],
					"text" : "64"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-32",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "int", "bang" ],
					"patching_rect" : [ 608.0, 502.0, 61.0, 22.0 ],
					"text" : "t i b"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-31",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"patching_rect" : [ 608.0, 617.0, 88.0, 22.0 ],
					"text" : "zl group"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-30",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"patching_rect" : [ 608.0, 475.0, 61.0, 22.0 ],
					"text" : "zl iter 1"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-28",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"patching_rect" : [ 608.0, 584.0, 61.0, 22.0 ],
					"text" : "zl join"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-25",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 612.0, 759.399999797344208, 100.0, 22.0 ],
					"text" : "pack"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-18",
					"maxclass" : "newobj",
					"numinlets" : 3,
					"numoutlets" : 0,
					"patching_rect" : [ 612.0, 794.799999594688416, 100.0, 22.0 ],
					"text" : "noteout"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-14",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 608.0, 643.0, 88.0, 22.0 ],
					"text" : "prepend chord"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-10",
					"maxclass" : "kslider",
					"mode" : 1,
					"numinlets" : 2,
					"numoutlets" : 2,
					"outlettype" : [ "int", "int" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 612.0, 690.0, 336.0, 53.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-79",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"patching_rect" : [ 541.0, 44.5, 100.0, 22.0 ],
					"text" : "t s s"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-78",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 753.0, 375.0, 54.0, 20.0 ],
					"text" : "octave"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-76",
					"maxclass" : "number",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 718.0, 347.0, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-72",
					"linecount" : 3,
					"maxclass" : "newobj",
					"numinlets" : 3,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 608.0, 375.0, 129.0, 49.0 ],
					"text" : "vexpr ($i1+ $i2) + 12*$i3 @scalarmode 1"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-67",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 608.0, 198.0, 100.0, 22.0 ],
					"text" : "prepend symbol"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-64",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 4,
					"outlettype" : [ "", "", "", "" ],
					"patching_rect" : [ 608.0, 247.0, 70.0, 22.0 ],
					"saved_object_attributes" : 					{
						"embed" : 0,
						"precision" : 6
					}
,
					"text" : "coll pitch"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-63",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 811.549999999999955, 204.5, 96.0, 22.0 ],
					"text" : "prepend symbol"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-60",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "", "", "" ],
					"patching_rect" : [ 746.75, 132.5, 59.0, 22.0 ],
					"text" : "unjoin"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-47",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"patching_rect" : [ 746.75, 104.5, 57.0, 22.0 ],
					"text" : "zl.rot -2"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-40",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 5,
					"outlettype" : [ "", "", "", "", "" ],
					"patching_rect" : [ 708.0, 78.0, 174.0, 22.0 ],
					"text" : "regexp ^(.)(b|#)?(.*)$"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-34",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 5,
					"outlettype" : [ "", "", "", "", "" ],
					"patching_rect" : [ 541.0, 78.0, 153.0, 22.0 ],
					"text" : "regexp ^([A-Za-z])([#b]?)"
				}

			}
, 			{
				"box" : 				{
					"coll_data" : 					{
						"count" : 108,
						"data" : [ 							{
								"key" : "M",
								"value" : [ 0, 4, 7 ]
							}
, 							{
								"key" : "m",
								"value" : [ 0, 3, 7 ]
							}
, 							{
								"key" : "dim",
								"value" : [ 0, 3, 6 ]
							}
, 							{
								"key" : "aug",
								"value" : [ 0, 4, 8 ]
							}
, 							{
								"key" : "sus2",
								"value" : [ 0, 2, 7 ]
							}
, 							{
								"key" : "sus4",
								"value" : [ 0, 5, 7 ]
							}
, 							{
								"key" : "m+",
								"value" : [ 0, 3, 8 ]
							}
, 							{
								"key" : "b5",
								"value" : [ 0, 4, 6 ]
							}
, 							{
								"key" : "m7_omit5",
								"value" : [ 0, 3, 10 ]
							}
, 							{
								"key" : "add9_omit3",
								"value" : [ 0, 7, 14 ]
							}
, 							{
								"key" : "7_omit3",
								"value" : [ 0, 7, 10 ]
							}
, 							{
								"key" : "9+5",
								"value" : [ 0, 10, 13 ]
							}
, 							{
								"key" : "m9+5",
								"value" : [ 0, 10, 14 ]
							}
, 							{
								"key" : "M7",
								"value" : [ 0, 4, 7, 11 ]
							}
, 							{
								"key" : "M6",
								"value" : [ 0, 4, 7, 9 ]
							}
, 							{
								"key" : "m7",
								"value" : [ 0, 3, 7, 10 ]
							}
, 							{
								"key" : "m6",
								"value" : [ 0, 3, 7, 9 ]
							}
, 							{
								"key" : "mM6",
								"value" : [ 0, 3, 7, 6 ]
							}
, 							{
								"key" : "+M7",
								"value" : [ 0, 4, 8, 11 ]
							}
, 							{
								"key" : 6,
								"value" : [ 0, 4, 7, 6 ]
							}
, 							{
								"key" : 7,
								"value" : [ 0, 4, 7, 10 ]
							}
, 							{
								"key" : "7+",
								"value" : [ 0, 4, 8, 10 ]
							}
, 							{
								"key" : "dim7",
								"value" : [ 0, 3, 6, 9, 11 ]
							}
, 							{
								"key" : "msus",
								"value" : [ 0, 3, 5, 7 ]
							}
, 							{
								"key" : "m(sus9)",
								"value" : [ 0, 3, 7, 14 ]
							}
, 							{
								"key" : "m7+5",
								"value" : [ 0, 3, 8, 10 ]
							}
, 							{
								"key" : "mM7",
								"value" : [ 0, 3, 7, 11 ]
							}
, 							{
								"key" : "m7b5",
								"value" : [ 0, 3, 6, 10 ]
							}
, 							{
								"key" : "mb9",
								"value" : [ 0, 3, 7, 13 ]
							}
, 							{
								"key" : "7sus4",
								"value" : [ 0, 5, 7, 10 ]
							}
, 							{
								"key" : "7sus2",
								"value" : [ 0, 2, 7, 10 ]
							}
, 							{
								"key" : "M7b5",
								"value" : [ 0, 4, 6, 11 ]
							}
, 							{
								"key" : "add9",
								"value" : [ 0, 4, 7, 14 ]
							}
, 							{
								"key" : "addb9",
								"value" : [ 0, 4, 7, 13 ]
							}
, 							{
								"key" : "7b5",
								"value" : [ 0, 4, 6, 10 ]
							}
, 							{
								"key" : "9b6",
								"value" : [ 0, 4, 8, 14 ]
							}
, 							{
								"key" : "add#9",
								"value" : [ 0, 4, 7, 15 ]
							}
, 							{
								"key" : "sus(add9)",
								"value" : [ 0, 5, 7, 14 ]
							}
, 							{
								"key" : "sus(addb9)",
								"value" : [ 0, 5, 7, 13 ]
							}
, 							{
								"key" : "sus(add#9)",
								"value" : [ 0, 5, 7, 15 ]
							}
, 							{
								"key" : "M9",
								"value" : [ 0, 4, 7, 11, 14 ]
							}
, 							{
								"key" : "m9",
								"value" : [ 0, 3, 7, 10, 14 ]
							}
, 							{
								"key" : "M13",
								"value" : [ 0, 4, 7, 11, 14, 17, 21 ]
							}
, 							{
								"key" : "m13",
								"value" : [ 0, 3, 7, 10, 14, 17, 21 ]
							}
, 							{
								"key" : 9,
								"value" : [ 0, 4, 7, 10, 14 ]
							}
, 							{
								"key" : 11,
								"value" : [ 0, 4, 7, 10, 14, 17 ]
							}
, 							{
								"key" : 13,
								"value" : [ 0, 4, 7, 10, 14, 17, 21 ]
							}
, 							{
								"key" : "+9M7",
								"value" : [ 0, 4, 8, 11, 14 ]
							}
, 							{
								"key" : "+9",
								"value" : [ 0, 4, 8, 10, 14 ]
							}
, 							{
								"key" : "+11",
								"value" : [ 0, 4, 8, 10, 14, 17 ]
							}
, 							{
								"key" : "9b5",
								"value" : [ 0, 4, 6, 10, 14 ]
							}
, 							{
								"key" : "6/9",
								"value" : [ 0, 4, 7, 14, 21 ]
							}
, 							{
								"key" : "13b5",
								"value" : [ 0, 4, 6, 10, 20 ]
							}
, 							{
								"key" : "M7#11",
								"value" : [ 0, 4, 7, 11, 18 ]
							}
, 							{
								"key" : "m9b5",
								"value" : [ 0, 3, 6, 10, 14 ]
							}
, 							{
								"key" : "m7b9",
								"value" : [ 0, 3, 7, 10, 13 ]
							}
, 							{
								"key" : "m7sus4",
								"value" : [ 0, 3, 5, 7, 10 ]
							}
, 							{
								"key" : "m7#9",
								"value" : [ 0, 3, 7, 10, 15 ]
							}
, 							{
								"key" : "m7(add13)",
								"value" : [ 0, 3, 7, 10, 21 ]
							}
, 							{
								"key" : "m7(add11)",
								"value" : [ 0, 3, 7, 10, 17 ]
							}
, 							{
								"key" : "mM7(add9)",
								"value" : [ 0, 3, 7, 11, 14 ]
							}
, 							{
								"key" : "m6(add9)",
								"value" : [ 0, 3, 7, 14, 21 ]
							}
, 							{
								"key" : "m+7b9",
								"value" : [ 0, 3, 8, 10, 13 ]
							}
, 							{
								"key" : "m+7#9",
								"value" : [ 0, 3, 8, 10, 15 ]
							}
, 							{
								"key" : "m7b5b9",
								"value" : [ 0, 3, 6, 10, 13 ]
							}
, 							{
								"key" : "7(6)",
								"value" : [ 0, 4, 7, 9, 10 ]
							}
, 							{
								"key" : "7#11",
								"value" : [ 0, 4, 7, 10, 18 ]
							}
, 							{
								"key" : "7(add13)",
								"value" : [ 0, 4, 7, 10, 21 ]
							}
, 							{
								"key" : "7+9",
								"value" : [ 0, 4, 7, 10, 15 ]
							}
, 							{
								"key" : "7b9",
								"value" : [ 0, 4, 7, 10, 13 ]
							}
, 							{
								"key" : "7b9sus",
								"value" : [ 0, 5, 7, 10, 13 ]
							}
, 							{
								"key" : "7b13",
								"value" : [ 0, 4, 7, 10, 20 ]
							}
, 							{
								"key" : "7b5#9",
								"value" : [ 0, 4, 6, 10, 15 ]
							}
, 							{
								"key" : "7b5b9",
								"value" : [ 0, 4, 6, 10, 13 ]
							}
, 							{
								"key" : "7b5(add13)",
								"value" : [ 0, 4, 6, 10, 21 ]
							}
, 							{
								"key" : "+7#9",
								"value" : [ 0, 4, 8, 10, 15 ]
							}
, 							{
								"key" : "7alt",
								"value" : [ 0, 4, 6, 10, 13 ]
							}
, 							{
								"key" : "dim(b13)",
								"value" : [ 0, 3, 6, 9, 8 ]
							}
, 							{
								"key" : "aug7b9",
								"value" : [ 0, 4, 8, 10, 13 ]
							}
, 							{
								"key" : "sus9",
								"value" : [ 0, 5, 7, 10, 14 ]
							}
, 							{
								"key" : "M11",
								"value" : [ 0, 4, 7, 11, 14, 17 ]
							}
, 							{
								"key" : "mM11",
								"value" : [ 0, 3, 7, 11, 14, 17 ]
							}
, 							{
								"key" : "m11",
								"value" : [ 0, 3, 7, 10, 14, 17 ]
							}
, 							{
								"key" : "+M11",
								"value" : [ 0, 4, 8, 11, 14, 17 ]
							}
, 							{
								"key" : "Ã˜11",
								"value" : [ 0, 3, 6, 10, 13, 17 ]
							}
, 							{
								"key" : "Â°11",
								"value" : [ 0, 3, 6, 9, 13, 16 ]
							}
, 							{
								"key" : "M13#11",
								"value" : [ 0, 4, 7, 11, 18, 21 ]
							}
, 							{
								"key" : "M9#11",
								"value" : [ 0, 4, 7, 11, 14, 18 ]
							}
, 							{
								"key" : "m7b9#11",
								"value" : [ 0, 3, 7, 10, 13, 18 ]
							}
, 							{
								"key" : "m+7b9#11",
								"value" : [ 0, 3, 8, 10, 13, 18 ]
							}
, 							{
								"key" : "m11+",
								"value" : [ 0, 3, 7, 10, 14, 18 ]
							}
, 							{
								"key" : "m11b5",
								"value" : [ 0, 3, 6, 10, 14, 17 ]
							}
, 							{
								"key" : "7#9#11",
								"value" : [ 0, 4, 7, 10, 15, 18 ]
							}
, 							{
								"key" : "7#9b13",
								"value" : [ 0, 4, 7, 10, 15, 20 ]
							}
, 							{
								"key" : "+7b9#11",
								"value" : [ 0, 4, 8, 10, 13, 18 ]
							}
, 							{
								"key" : "7b9#11",
								"value" : [ 0, 4, 7, 10, 13, 18 ]
							}
, 							{
								"key" : "11+",
								"value" : [ 0, 4, 7, 10, 14, 18 ]
							}
, 							{
								"key" : "11b9",
								"value" : [ 0, 4, 7, 10, 13, 17 ]
							}
, 							{
								"key" : "13#11",
								"value" : [ 0, 4, 7, 10, 18, 21 ]
							}
, 							{
								"key" : "13#9",
								"value" : [ 0, 4, 7, 10, 15, 21 ]
							}
, 							{
								"key" : "13sus",
								"value" : [ 0, 5, 7, 10, 14, 21 ]
							}
, 							{
								"key" : "13susb9",
								"value" : [ 0, 5, 7, 10, 13, 21 ]
							}
, 							{
								"key" : "M7(add13)",
								"value" : [ 0, 4, 7, 10, 13, 21 ]
							}
, 							{
								"key" : "WTCluster",
								"value" : [ 0, 2, 4, 6, 8, 10 ]
							}
, 							{
								"key" : "mM13",
								"value" : [ 0, 3, 7, 11, 14, 17, 21 ]
							}
, 							{
								"key" : "+M13",
								"value" : [ 0, 4, 8, 11, 14, 17, 21 ]
							}
, 							{
								"key" : "+13",
								"value" : [ 0, 4, 8, 10, 14, 17, 21 ]
							}
, 							{
								"key" : "dim13",
								"value" : [ 0, 3, 6, 10, 14, 17, 21 ]
							}
 ]
					}
,
					"id" : "obj-12",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 4,
					"outlettype" : [ "", "", "", "" ],
					"patching_rect" : [ 779.149999999999977, 247.0, 100.0, 22.0 ],
					"saved_object_attributes" : 					{
						"embed" : 1,
						"precision" : 6
					}
,
					"text" : "coll chord-lib"
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.12775145471096, 0.999752759933472, 0.999038398265839, 1.0 ],
					"id" : "obj-6",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 29.5, 378.0, 36.0, 36.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 266.0, 126.5, 36.0, 36.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-5",
					"linecount" : 2,
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 45.0, 113.5, 105.0, 33.0 ],
					"presentation" : 1,
					"presentation_linecount" : 2,
					"presentation_rect" : [ 84.0, 131.0, 105.0, 33.0 ],
					"text" : "compute Transition Matrix"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-114",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patcher" : 					{
						"fileversion" : 1,
						"appversion" : 						{
							"major" : 8,
							"minor" : 5,
							"revision" : 5,
							"architecture" : "x64",
							"modernui" : 1
						}
,
						"classnamespace" : "box",
						"rect" : [ 181.0, 62.0, 788.0, 832.0 ],
						"bglocked" : 0,
						"openinpresentation" : 0,
						"default_fontsize" : 12.0,
						"default_fontface" : 0,
						"default_fontname" : "Arial",
						"gridonopen" : 1,
						"gridsize" : [ 15.0, 15.0 ],
						"gridsnaponopen" : 1,
						"objectsnaponopen" : 1,
						"statusbarvisible" : 2,
						"toolbarvisible" : 1,
						"lefttoolbarpinned" : 0,
						"toptoolbarpinned" : 0,
						"righttoolbarpinned" : 0,
						"bottomtoolbarpinned" : 0,
						"toolbars_unpinned_last_save" : 0,
						"tallnewobj" : 0,
						"boxanimatetime" : 200,
						"enablehscroll" : 1,
						"enablevscroll" : 1,
						"devicewidth" : 0.0,
						"description" : "",
						"digest" : "",
						"tags" : "",
						"style" : "",
						"subpatcher_template" : "",
						"assistshowspatchername" : 0,
						"boxes" : [ 							{
								"box" : 								{
									"id" : "obj-38",
									"linecount" : 2,
									"maxclass" : "newobj",
									"numinlets" : 2,
									"numoutlets" : 2,
									"outlettype" : [ "", "" ],
									"patching_rect" : [ 50.0, 150.0, 100.0, 35.0 ],
									"text" : "bach.filternull @out t"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-30",
									"maxclass" : "newobj",
									"numinlets" : 1,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 290.0, 390.0, 100.0, 22.0 ],
									"saved_object_attributes" : 									{
										"versionnumber" : 80100
									}
,
									"text" : "bach.wrap"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-29",
									"maxclass" : "message",
									"numinlets" : 2,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 338.5, 319.0, 21.0, 22.0 ],
									"text" : "0"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-28",
									"maxclass" : "message",
									"numinlets" : 2,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 290.0, 319.0, 21.0, 22.0 ],
									"text" : "1"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-26",
									"maxclass" : "newobj",
									"numinlets" : 2,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 290.0, 355.5, 100.0, 22.0 ],
									"text" : "gate"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-25",
									"maxclass" : "newobj",
									"numinlets" : 2,
									"numoutlets" : 2,
									"outlettype" : [ "bang", "" ],
									"patching_rect" : [ 290.0, 286.0, 67.5, 22.0 ],
									"text" : "sel null"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-21",
									"linecount" : 2,
									"maxclass" : "newobj",
									"numinlets" : 3,
									"numoutlets" : 3,
									"outlettype" : [ "", "", "" ],
									"patching_rect" : [ 290.0, 233.0, 76.0, 35.0 ],
									"saved_object_attributes" : 									{
										"versionnumber" : 80100
									}
,
									"text" : "bach.find X @out t"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-107",
									"maxclass" : "newobj",
									"numinlets" : 1,
									"numoutlets" : 2,
									"outlettype" : [ "", "" ],
									"patching_rect" : [ 290.0, 169.0, 100.0, 22.0 ],
									"text" : "t l l"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-91",
									"maxclass" : "newobj",
									"numinlets" : 2,
									"numoutlets" : 2,
									"outlettype" : [ "", "" ],
									"patching_rect" : [ 50.0, 119.0, 259.0, 22.0 ],
									"saved_object_attributes" : 									{
										"versionnumber" : 80100
									}
,
									"text" : "bach.mapelem @maxdepth 1"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-78",
									"maxclass" : "newobj",
									"numinlets" : 1,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 290.0, 145.0, 100.0, 22.0 ],
									"saved_object_attributes" : 									{
										"versionnumber" : 80100
									}
,
									"text" : "bach.flat"
								}

							}
, 							{
								"box" : 								{
									"comment" : "",
									"id" : "obj-111",
									"index" : 1,
									"maxclass" : "inlet",
									"numinlets" : 0,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 50.0, 71.0, 30.0, 30.0 ]
								}

							}
, 							{
								"box" : 								{
									"comment" : "",
									"id" : "obj-112",
									"index" : 1,
									"maxclass" : "outlet",
									"numinlets" : 1,
									"numoutlets" : 0,
									"patching_rect" : [ 50.0, 192.0, 30.0, 30.0 ]
								}

							}
 ],
						"lines" : [ 							{
								"patchline" : 								{
									"destination" : [ "obj-21", 0 ],
									"midpoints" : [ 380.5, 220.5, 299.5, 220.5 ],
									"source" : [ "obj-107", 1 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-26", 1 ],
									"midpoints" : [ 299.5, 205.75, 380.5, 205.75 ],
									"source" : [ "obj-107", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-91", 0 ],
									"source" : [ "obj-111", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-25", 0 ],
									"source" : [ "obj-21", 1 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-28", 0 ],
									"source" : [ "obj-25", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-29", 0 ],
									"source" : [ "obj-25", 1 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-30", 0 ],
									"source" : [ "obj-26", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-26", 0 ],
									"source" : [ "obj-28", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-26", 0 ],
									"source" : [ "obj-29", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-91", 1 ],
									"midpoints" : [ 299.5, 435.0, 407.5, 435.0, 407.5, 108.0, 299.5, 108.0 ],
									"source" : [ "obj-30", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-112", 0 ],
									"source" : [ "obj-38", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-107", 0 ],
									"source" : [ "obj-78", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-38", 0 ],
									"source" : [ "obj-91", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-78", 0 ],
									"source" : [ "obj-91", 1 ]
								}

							}
 ]
					}
,
					"patching_rect" : [ 29.5, 272.5, 119.5, 22.0 ],
					"saved_object_attributes" : 					{
						"description" : "",
						"digest" : "",
						"globalpatchername" : "",
						"tags" : ""
					}
,
					"text" : "p transition remover"
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.985537528991699, 0.009297370910645, 0.999170780181885, 1.0 ],
					"bgcolor2" : [ 0.2, 0.2, 0.2, 1.0 ],
					"bgfillcolor_angle" : 270.0,
					"bgfillcolor_autogradient" : 0.0,
					"bgfillcolor_color" : [ 0.985537528991699, 0.009297370910645, 0.999170780181885, 1.0 ],
					"bgfillcolor_color1" : [ 0.985537528991699, 0.009297370910645, 0.999170780181885, 1.0 ],
					"bgfillcolor_color2" : [ 0.2, 0.2, 0.2, 1.0 ],
					"bgfillcolor_proportion" : 0.5,
					"bgfillcolor_type" : "gradient",
					"fontsize" : 20.0,
					"gradient" : 1,
					"id" : "obj-22",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 208.0, 79.0, 76.0, 31.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 47.0, 78.5, 76.0, 31.0 ],
					"text" : "dump",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"coll_data" : 					{
						"count" : 27,
						"data" : [ 							{
								"key" : 1,
								"value" : [ "CM", "F#M", "CM", "F#M", "X" ]
							}
, 							{
								"key" : 2,
								"value" : [ "CM", "GM", "DM", "Em", "D9", "G9", "CM", "GM", "DM", "Em", "F#M", "X" ]
							}
, 							{
								"key" : 3,
								"value" : [ "Am", "Cm", "D#m", "F#m", "Am", "Cm", "D#m", "A#m", "X" ]
							}
, 							{
								"key" : 4,
								"value" : [ "DM", "Fadd9", "CM", "Am", "DM", "Fadd9", "CM", "Am", "F#M", "CM", "F#M", "CM", "X" ]
							}
, 							{
								"key" : 5,
								"value" : [ "CM", "GM", "DM", "CM", "GM", "Gadd9", "DM", "X" ]
							}
, 							{
								"key" : 6,
								"value" : [ "Am", "Bm", "C#m", "D#m", "Fm", "Gm", "Am", "Bm", "C#m", "D#m", "Fm", "Gm", "X" ]
							}
, 							{
								"key" : 7,
								"value" : [ "CM", "EM", "G#M", "CM", "EM", "G#M", "X" ]
							}
, 							{
								"key" : 8,
								"value" : [ "Cm", "Gm", "Dm", "Am", "Em", "Bm", "F#m", "C#m", "G#m", "D#m", "A#m", "Fm", "Cm", "Gm", "Fm", "Gm", "Dm", "Am", "Em", "Bm", "F#m", "C#m", "G#m", "C#m", "Am", "Cm", "X" ]
							}
, 							{
								"key" : 9,
								"value" : [ "C7", "F7", "A#7", "D#7", "C#7", "F#7", "B7", "E7", "A7", "D7", "G7", "C7", "F7", "A#7", "D#7", "C#7", "F#7", "B7", "E7", "A7", "D7", "G7", "X" ]
							}
, 							{
								"key" : 10,
								"value" : [ "CM", "A#M", "Am7", "FM", "CM", "A#M", "Am7", "FM", "C#dim", "A#M", "Am7", "FM", "Am", "FM", "X" ]
							}
, 							{
								"key" : 11,
								"value" : [ "CM", "D7add11", "CM", "G7add9", "CM", "Dm7", "CM", "Dm7", "CM", "GM", "X" ]
							}
, 							{
								"key" : 12,
								"value" : [ "Gadd9", "Fadd9", "Gadd9", "Fadd9", "Gadd9", "DM", "Fadd9", "Em+", "Fadd9", "Gadd9", "X" ]
							}
, 							{
								"key" : 13,
								"value" : [ "CM", "Cadd11", "CM", "Cadd11", "D#add11", "D#M", "D#add11", "CM", "G#M", "CM", "X" ]
							}
, 							{
								"key" : 14,
								"value" : [ "Am", "FM", "DM", "Em", "Bm7", "EM", "Am", "DM", "Am", "Em", "X" ]
							}
, 							{
								"key" : 15,
								"value" : [ "FM7", "G6", "Am", "G6", "FM7", "X" ]
							}
, 							{
								"key" : 16,
								"value" : [ "FM", "Fadd9", "Gadd9", "FM", "Fadd9", "FM", "GM", "GM6", "Amadd9", "Amadd9", "Gadd11", "GM", "Gadd9", "FM", "FM", "Gadd11", "Gadd11", "Amadd9", "Amadd9", "FM7", "FM7", "G6", "X" ]
							}
, 							{
								"key" : 17,
								"value" : [ "CM", "Cadd11", "CM", "Cadd11", "X" ]
							}
, 							{
								"key" : 18,
								"value" : [ "Am", "Fm", "Am", "G#M", "CM", "FM", "C#7", "FM", "GM", "X" ]
							}
, 							{
								"key" : 19,
								"value" : [ "C9", "F9", "A#9", "D#9", "C#9", "F#9", "B9", "E9", "A9", "D9", "G9", "C9", "F9", "A#9", "D#9", "C#9", "F#9", "B9", "E9", "A9", "D9", "G9", "X" ]
							}
, 							{
								"key" : 20,
								"value" : [ "Am", "Cm", "D#m11", "F#m11", "Am11", "Cm11", "D#m11", "A#m", "Am", "Cm", "X" ]
							}
, 							{
								"key" : 21,
								"value" : [ "FM7", "G6", "FM7", "G6", "Am11", "G6", "FM7", "X" ]
							}
, 							{
								"key" : 22,
								"value" : [ "Am", "Dadd9", "Em11", "Bm7", "Eadd9", "Am9", "Dadd9", "Am11", "Em9", "Am", "Em", "X" ]
							}
, 							{
								"key" : 23,
								"value" : [ "FM", "GM", "CM", "C6add11", "FM", "G#dim", "CM", "F#M", "CM", "X" ]
							}
, 							{
								"key" : 24,
								"value" : [ "CM", "GM", "D#dim", "Em", "G7", "CM", "G7", "GM", "D#dim", "Em", "F#M", "CM", "F#M", "CM", "GM", "X" ]
							}
, 							{
								"key" : 25,
								"value" : [ "Am", "DM", "Em", "Bm7", "E#dim", "Am", "Bm", "X" ]
							}
, 							{
								"key" : 26,
								"value" : [ "EM", "G#M", "EM", "G#M", "AM", "EM", "G#M", "X" ]
							}
, 							{
								"key" : 27,
								"value" : [ "FM", "GM", "CM", "FM", "GM", "CM", "X" ]
							}
 ]
					}
,
					"id" : "obj-17",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 4,
					"outlettype" : [ "", "", "", "" ],
					"patching_rect" : [ 208.0, 119.0, 100.0, 22.0 ],
					"saved_object_attributes" : 					{
						"embed" : 1,
						"precision" : 6
					}
,
					"text" : "coll songs-library"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-16",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 0,
					"patching_rect" : [ 29.5, 599.0, 100.0, 22.0 ],
					"text" : "print new state"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-15",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 194.5, 488.0, 80.0, 22.0 ],
					"text" : "print ERROR"
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-9",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 208.0, 318.0, 163.0, 23.0 ],
					"saved_object_attributes" : 					{
						"versionnumber" : 80100
					}
,
					"text" : "bach.print TransitionMatrix"
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-19",
					"maxclass" : "newobj",
					"numinlets" : 3,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"patching_rect" : [ 29.5, 444.0, 184.0, 23.0 ],
					"text" : "cage.markov.synthesis @out t"
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 1.0, 0.007843137254902, 0.007843137254902, 1.0 ],
					"bgcolor2" : [ 0.2, 0.2, 0.2, 1.0 ],
					"bgfillcolor_angle" : 270.0,
					"bgfillcolor_autogradient" : 0.0,
					"bgfillcolor_color" : [ 1.0, 0.007843137254902, 0.007843137254902, 1.0 ],
					"bgfillcolor_color1" : [ 1.0, 0.007843137254902, 0.007843137254902, 1.0 ],
					"bgfillcolor_color2" : [ 0.2, 0.2, 0.2, 1.0 ],
					"bgfillcolor_proportion" : 0.5,
					"bgfillcolor_type" : "gradient",
					"fontsize" : 20.0,
					"gradient" : 1,
					"id" : "obj-13",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 180.0, 188.0, 76.0, 31.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 334.0, 43.5, 76.0, 31.0 ],
					"text" : "clear",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.12775145471096, 0.999752759933472, 0.999038398265839, 1.0 ],
					"id" : "obj-11",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 29.5, 73.5, 36.0, 36.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 47.0, 126.5, 36.0, 36.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-70",
					"linecount" : 2,
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 29.5, 227.5, 136.0, 38.0 ],
					"text" : "cage.markov.analysis @order 1"
				}

			}
, 			{
				"box" : 				{
					"angle" : 270.0,
					"grad1" : [ 0.533333333333333, 1.0, 0.486274509803922, 1.0 ],
					"grad2" : [ 0.541176470588235, 0.811764705882353, 1.0, 1.0 ],
					"id" : "obj-56",
					"maxclass" : "panel",
					"mode" : 1,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 194.5, 590.0, 33.0, 31.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 0.0, -7.0, 450.0, 268.0 ],
					"proportion" : 0.5
				}

			}
 ],
		"lines" : [ 			{
				"patchline" : 				{
					"destination" : [ "obj-25", 1 ],
					"source" : [ "obj-10", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-25", 0 ],
					"source" : [ "obj-10", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.12775145471096, 0.999752759933472, 0.999038398265839, 1.0 ],
					"destination" : [ "obj-70", 0 ],
					"source" : [ "obj-11", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-19", 1 ],
					"midpoints" : [ 39.0, 314.5, 121.5, 314.5 ],
					"order" : 1,
					"source" : [ "obj-114", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 0 ],
					"midpoints" : [ 39.0, 303.25, 217.5, 303.25 ],
					"order" : 0,
					"source" : [ "obj-114", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-42", 0 ],
					"order" : 1,
					"source" : [ "obj-12", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-68", 1 ],
					"order" : 0,
					"source" : [ "obj-12", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-72", 1 ],
					"midpoints" : [ 788.649999999999977, 335.5, 672.5, 335.5 ],
					"order" : 2,
					"source" : [ "obj-12", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.50196647644043, 0.001480937004089, 0.998501121997833, 1.0 ],
					"destination" : [ "obj-19", 0 ],
					"midpoints" : [ 189.5, 435.0, 39.0, 435.0 ],
					"order" : 0,
					"source" : [ "obj-13", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.50196647644043, 0.001480937004089, 0.998501121997833, 1.0 ],
					"destination" : [ "obj-70", 0 ],
					"midpoints" : [ 189.5, 221.0, 39.0, 221.0 ],
					"order" : 1,
					"source" : [ "obj-13", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-10", 0 ],
					"disabled" : 1,
					"source" : [ "obj-14", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.985537528991699, 0.009297370910645, 0.999170780181885, 1.0 ],
					"destination" : [ "obj-70", 0 ],
					"midpoints" : [ 217.5, 154.75, 39.0, 154.75 ],
					"source" : [ "obj-17", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-15", 0 ],
					"source" : [ "obj-19", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-16", 0 ],
					"order" : 3,
					"source" : [ "obj-19", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-23", 0 ],
					"order" : 2,
					"source" : [ "obj-19", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-51", 1 ],
					"midpoints" : [ 39.0, 470.0, 15.0, 470.0, 15.0, 152.0, 465.0, 152.0, 465.0, 152.0, 518.5, 152.0 ],
					"order" : 1,
					"source" : [ "obj-19", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-79", 0 ],
					"midpoints" : [ 39.0, 532.0, 433.0, 532.0, 433.0, 34.0, 550.5, 34.0 ],
					"order" : 0,
					"source" : [ "obj-19", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-17", 0 ],
					"source" : [ "obj-22", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-18", 0 ],
					"source" : [ "obj-25", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-31", 0 ],
					"source" : [ "obj-28", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-6", 0 ],
					"source" : [ "obj-3", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-32", 0 ],
					"source" : [ "obj-30", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-14", 0 ],
					"source" : [ "obj-31", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-28", 0 ],
					"source" : [ "obj-32", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 0 ],
					"source" : [ "obj-32", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-67", 0 ],
					"source" : [ "obj-34", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-28", 1 ],
					"source" : [ "obj-35", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-41", 0 ],
					"source" : [ "obj-37", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-30", 0 ],
					"source" : [ "obj-38", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-37", 0 ],
					"source" : [ "obj-38", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-47", 0 ],
					"source" : [ "obj-40", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-31", 1 ],
					"source" : [ "obj-41", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-70", 0 ],
					"midpoints" : [ 304.5, 290.0, 179.0, 290.0, 179.0, 212.0, 39.0, 212.0 ],
					"source" : [ "obj-43", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-43", 0 ],
					"source" : [ "obj-46", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-60", 0 ],
					"source" : [ "obj-47", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-11", 0 ],
					"source" : [ "obj-48", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-22", 0 ],
					"source" : [ "obj-48", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-48", 0 ],
					"source" : [ "obj-50", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-46", 0 ],
					"source" : [ "obj-55", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-17", 0 ],
					"source" : [ "obj-59", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.12775145471096, 0.999752759933472, 0.999038398265839, 1.0 ],
					"destination" : [ "obj-19", 0 ],
					"source" : [ "obj-6", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-90", 0 ],
					"source" : [ "obj-60", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-12", 0 ],
					"source" : [ "obj-63", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-72", 0 ],
					"source" : [ "obj-64", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-64", 0 ],
					"source" : [ "obj-67", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-114", 0 ],
					"source" : [ "obj-70", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-38", 0 ],
					"order" : 2,
					"source" : [ "obj-72", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-65", 0 ],
					"order" : 1,
					"source" : [ "obj-72", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-66", 1 ],
					"order" : 0,
					"source" : [ "obj-72", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-76", 0 ],
					"source" : [ "obj-73", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-72", 2 ],
					"source" : [ "obj-76", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-34", 0 ],
					"source" : [ "obj-79", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-40", 0 ],
					"source" : [ "obj-79", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-12", 0 ],
					"source" : [ "obj-90", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-63", 0 ],
					"source" : [ "obj-90", 4 ]
				}

			}
 ],
		"styles" : [ 			{
				"name" : "rnbodefault",
				"default" : 				{
					"accentcolor" : [ 0.343034118413925, 0.506230533123016, 0.86220508813858, 1.0 ],
					"bgcolor" : [ 0.031372549019608, 0.125490196078431, 0.211764705882353, 1.0 ],
					"bgfillcolor" : 					{
						"angle" : 270.0,
						"autogradient" : 0.0,
						"color" : [ 0.031372549019608, 0.125490196078431, 0.211764705882353, 1.0 ],
						"color1" : [ 0.031372549019608, 0.125490196078431, 0.211764705882353, 1.0 ],
						"color2" : [ 0.263682, 0.004541, 0.038797, 1.0 ],
						"proportion" : 0.39,
						"type" : "color"
					}
,
					"color" : [ 0.929412, 0.929412, 0.352941, 1.0 ],
					"elementcolor" : [ 0.357540726661682, 0.515565991401672, 0.861786782741547, 1.0 ],
					"fontname" : [ "Lato" ],
					"fontsize" : [ 12.0 ],
					"stripecolor" : [ 0.258338063955307, 0.352425158023834, 0.511919498443604, 1.0 ]
				}
,
				"parentstyle" : "",
				"multi" : 0
			}
, 			{
				"name" : "rnbolight",
				"default" : 				{
					"accentcolor" : [ 0.443137254901961, 0.505882352941176, 0.556862745098039, 1.0 ],
					"bgcolor" : [ 0.796078431372549, 0.862745098039216, 0.925490196078431, 1.0 ],
					"bgfillcolor" : 					{
						"angle" : 270.0,
						"autogradient" : 0.0,
						"color" : [ 0.835294117647059, 0.901960784313726, 0.964705882352941, 1.0 ],
						"color1" : [ 0.031372549019608, 0.125490196078431, 0.211764705882353, 1.0 ],
						"color2" : [ 0.263682, 0.004541, 0.038797, 1.0 ],
						"proportion" : 0.39,
						"type" : "color"
					}
,
					"clearcolor" : [ 0.898039, 0.898039, 0.898039, 1.0 ],
					"color" : [ 0.815686274509804, 0.509803921568627, 0.262745098039216, 1.0 ],
					"editing_bgcolor" : [ 0.898039, 0.898039, 0.898039, 1.0 ],
					"elementcolor" : [ 0.337254901960784, 0.384313725490196, 0.462745098039216, 1.0 ],
					"fontname" : [ "Lato" ],
					"locked_bgcolor" : [ 0.898039, 0.898039, 0.898039, 1.0 ],
					"stripecolor" : [ 0.309803921568627, 0.698039215686274, 0.764705882352941, 1.0 ],
					"textcolor_inverse" : [ 0.0, 0.0, 0.0, 1.0 ]
				}
,
				"parentstyle" : "",
				"multi" : 0
			}
, 			{
				"name" : "rnbomonokai",
				"default" : 				{
					"accentcolor" : [ 0.501960784313725, 0.501960784313725, 0.501960784313725, 1.0 ],
					"bgcolor" : [ 0.0, 0.0, 0.0, 1.0 ],
					"bgfillcolor" : 					{
						"angle" : 270.0,
						"autogradient" : 0.0,
						"color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"color1" : [ 0.031372549019608, 0.125490196078431, 0.211764705882353, 1.0 ],
						"color2" : [ 0.263682, 0.004541, 0.038797, 1.0 ],
						"proportion" : 0.39,
						"type" : "color"
					}
,
					"clearcolor" : [ 0.976470588235294, 0.96078431372549, 0.917647058823529, 1.0 ],
					"color" : [ 0.611764705882353, 0.125490196078431, 0.776470588235294, 1.0 ],
					"editing_bgcolor" : [ 0.976470588235294, 0.96078431372549, 0.917647058823529, 1.0 ],
					"elementcolor" : [ 0.749019607843137, 0.83921568627451, 1.0, 1.0 ],
					"fontname" : [ "Lato" ],
					"locked_bgcolor" : [ 0.976470588235294, 0.96078431372549, 0.917647058823529, 1.0 ],
					"stripecolor" : [ 0.796078431372549, 0.207843137254902, 1.0, 1.0 ],
					"textcolor" : [ 0.129412, 0.129412, 0.129412, 1.0 ]
				}
,
				"parentstyle" : "",
				"multi" : 0
			}
 ]
	}

}
