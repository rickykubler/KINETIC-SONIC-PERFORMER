{
	"patcher" : 	{
		"fileversion" : 1,
		"appversion" : 		{
			"major" : 8,
			"minor" : 5,
			"revision" : 1,
			"architecture" : "x64",
			"modernui" : 1
		}
,
		"classnamespace" : "box",
		"rect" : [ 34.0, 62.0, 1350.0, 735.0 ],
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
		"boxes" : [ 			{
				"box" : 				{
					"id" : "obj-36",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 584.000017404556274, 530.333335697650909, 50.0, 22.0 ],
					"text" : "note $1"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-2",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 637.333352327346802, 530.333335697650909, 50.0, 22.0 ],
					"text" : "target 0"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-6",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "bang", "" ],
					"patching_rect" : [ 914.468457325981035, 475.035647801418236, 66.66666567325592, 22.0 ],
					"text" : "t b s"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-10",
					"maxclass" : "newobj",
					"numinlets" : 4,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 914.686891525359897, 445.868972025175026, 100.0, 22.0 ],
					"text" : "pak f f f f"
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-14",
					"linecount" : 2,
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 906.454714525360032, 342.666668832302094, 47.0, 36.0 ],
					"presentation_linecount" : 2,
					"text" : "attack time",
					"textcolor" : [ 0.501961, 0.501961, 0.501961, 1.0 ],
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-23",
					"linecount" : 2,
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 960.176943525360002, 342.666668832302094, 48.0, 36.0 ],
					"presentation_linecount" : 2,
					"text" : "decay time",
					"textcolor" : [ 0.501961, 0.501961, 0.501961, 1.0 ],
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-24",
					"linecount" : 2,
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1011.388063525359939, 342.666668832302094, 53.0, 36.0 ],
					"presentation_linecount" : 2,
					"text" : "sustain gain ",
					"textcolor" : [ 0.501961, 0.501961, 0.501961, 1.0 ],
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-26",
					"linecount" : 2,
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1064.121401525359943, 342.666668832302094, 55.0, 36.0 ],
					"presentation_linecount" : 2,
					"text" : "release time",
					"textcolor" : [ 0.501961, 0.501961, 0.501961, 1.0 ],
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"floatoutput" : 1,
					"id" : "obj-29",
					"maxclass" : "dial",
					"mult" : 0.01,
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "float" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 1022.620241525360143, 378.166668832302094, 30.535634999999999, 30.535634999999999 ],
					"size" : 100.0
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-31",
					"maxclass" : "dial",
					"mult" : 10.0,
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "float" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 1076.353579525360146, 378.166668832302094, 30.535634999999999, 30.535634999999999 ],
					"size" : 100.0
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-32",
					"maxclass" : "dial",
					"mult" : 10.0,
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "float" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 968.909120525360095, 378.166668832302094, 30.535634999999999, 30.535634999999999 ],
					"size" : 100.0
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-34",
					"maxclass" : "dial",
					"mult" : 10.0,
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "float" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 914.686891525359897, 378.166668832302094, 30.535634999999999, 30.535634999999999 ],
					"size" : 100.0
				}

			}
, 			{
				"box" : 				{
					"channels" : 1,
					"id" : "obj-5",
					"lastchannelcount" : 0,
					"maxclass" : "live.gain~",
					"numinlets" : 1,
					"numoutlets" : 4,
					"orientation" : 1,
					"outlettype" : [ "signal", "", "float", "list" ],
					"parameter_enable" : 1,
					"patching_rect" : [ 588.686884968848972, 608.750020384788513, 136.0, 30.0 ],
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_initial" : [ -18 ],
							"parameter_initial_enable" : 1,
							"parameter_longname" : "live.gain~[3]",
							"parameter_mmax" : 6.0,
							"parameter_mmin" : -70.0,
							"parameter_shortname" : "live.gain~",
							"parameter_type" : 0,
							"parameter_unitstyle" : 4
						}

					}
,
					"showname" : 0,
					"varname" : "live.gain~[3]"
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-33",
					"maxclass" : "newobj",
					"numinlets" : 3,
					"numoutlets" : 1,
					"outlettype" : [ "signal" ],
					"patching_rect" : [ 588.686884968848972, 566.166676998138428, 392.563131601242276, 23.0 ],
					"text" : "poly~ adsr-synth 10 @midimode 1 @zone 0"
				}

			}
, 			{
				"box" : 				{
					"hkeycolor" : [ 0.986246049404144, 0.007120788097382, 0.027434188872576, 1.0 ],
					"id" : "obj-119",
					"maxclass" : "kslider",
					"numinlets" : 2,
					"numoutlets" : 2,
					"outlettype" : [ "int", "int" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 34.833331227302551, 557.666662633419037, 504.0, 76.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontface" : 0,
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-116",
					"items" : [ "major", "scale", ",", "natural", "minor", "scale" ],
					"maxclass" : "umenu",
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "int", "", "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 438.833331227302551, 317.833339214324951, 100.0, 23.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-113",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 287.833331227302551, 415.33333545923233, 251.0, 22.0 ],
					"text" : "0 0, 1 2, 2 3, 3 5, 4 7, 5 8, 6 10, 7 12"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-109",
					"maxclass" : "newobj",
					"numinlets" : 3,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"patching_rect" : [ 539.500006914138794, 142.0, 100.0, 22.0 ],
					"text" : "line"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-110",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 539.500006914138794, 115.0, 50.0, 22.0 ],
					"text" : "$1 200"
				}

			}
, 			{
				"box" : 				{
					"floatoutput" : 1,
					"id" : "obj-111",
					"maxclass" : "slider",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 539.500006914138794, 196.0, 114.0, 38.5 ],
					"size" : 1.0
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-107",
					"maxclass" : "spectroscope~",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 761.833327174186707, 905.333360314369202, 478.0, 184.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-105",
					"maxclass" : "scope~",
					"numinlets" : 2,
					"numoutlets" : 0,
					"patching_rect" : [ 434.666671395301819, 902.583350896835327, 295.333338260650635, 189.500018835067749 ]
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontsize" : 40.0,
					"id" : "obj-104",
					"linecount" : 2,
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 201.666672825813293, 692.000007510185242, 170.333316802978516, 96.0 ],
					"text" : "FX - tremolo"
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontsize" : 40.0,
					"id" : "obj-85",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 237.333343505859375, 1048.833357930183411, 146.333316087722778, 51.0 ],
					"text" : "ADSR"
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontsize" : 40.0,
					"id" : "obj-84",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 596.499983906745911, 816.000007510185242, 146.333316087722778, 51.0 ],
					"text" : "SYNTH"
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontsize" : 40.0,
					"id" : "obj-83",
					"linecount" : 2,
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 359.166680812835693, 448.33333545923233, 179.666650414466858, 96.0 ],
					"text" : "MIDI manager"
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontsize" : 40.0,
					"id" : "obj-82",
					"linecount" : 2,
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 632.166673302650452, 58.000000357627869, 179.666650414466858, 96.0 ],
					"text" : "OSC receiver"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-78",
					"maxclass" : "number",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 40.999997615814209, 73.0, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-75",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 362.499984979629517, 169.0, 178.0, 20.0 ],
					"text" : "- - - freq from python  - - "
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-55",
					"maxclass" : "newobj",
					"numinlets" : 3,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"patching_rect" : [ 98.33333945274353, 751.000007510185242, 100.0, 22.0 ],
					"text" : "line"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-60",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 98.33333945274353, 722.000007510185242, 50.0, 22.0 ],
					"text" : "$1 100"
				}

			}
, 			{
				"box" : 				{
					"format" : 6,
					"id" : "obj-54",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 181.333341836929321, 828.000006318092346, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-48",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "signal" ],
					"patching_rect" : [ 52.24998950958252, 937.666674494743347, 65.083349943161011, 22.0 ],
					"text" : "*~"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-45",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "signal" ],
					"patching_rect" : [ 98.33333945274353, 896.000007510185242, 100.0, 22.0 ],
					"text" : "+~ 0.5"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-39",
					"maxclass" : "newobj",
					"numinlets" : 6,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 98.33333945274353, 795.500006318092346, 162.0, 22.0 ],
					"text" : "scale 1. 0. 0. 10."
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-37",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "signal" ],
					"patching_rect" : [ 98.33333945274353, 864.500006318092346, 100.0, 22.0 ],
					"text" : "cycle~"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-8",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"patching_rect" : [ 287.833331227302551, 325.33333545923233, 100.0, 22.0 ],
					"text" : "loadbang"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-3",
					"maxclass" : "newobj",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 98.33333945274353, 692.000007510185242, 70.249997615814209, 22.0 ],
					"text" : "r fx"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-1",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 539.500006914138794, 245.333333015441895, 41.5, 22.0 ],
					"text" : "s fx"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-66",
					"maxclass" : "newobj",
					"numinlets" : 3,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"patching_rect" : [ 154.249985098838806, 142.0, 100.0, 22.0 ],
					"text" : "line"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-67",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 154.249985098838806, 115.0, 50.0, 22.0 ],
					"text" : "$1 200"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-65",
					"maxclass" : "newobj",
					"numinlets" : 3,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"patching_rect" : [ 357.833315134048462, 142.0, 100.0, 22.0 ],
					"text" : "line"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-64",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 357.833315134048462, 115.0, 50.0, 22.0 ],
					"text" : "$1 200"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-57",
					"maxclass" : "newobj",
					"numinlets" : 5,
					"numoutlets" : 5,
					"outlettype" : [ "", "", "", "", "" ],
					"patching_rect" : [ 40.999997615814209, 44.333333253860474, 473.0, 22.0 ],
					"text" : "route on_off amp freq fx"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-43",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "int" ],
					"patching_rect" : [ 34.833331227302551, 448.33333545923233, 100.0, 22.0 ],
					"text" : "+ 48"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-42",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 321.833331227302551, 349.33333545923233, 87.0, 20.0 ],
					"text" : "major scale"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-40",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 202.833331227302551, 360.83333545923233, 50.0, 22.0 ],
					"text" : "clear"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-38",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 287.833331227302551, 374.83333545923233, 251.0, 22.0 ],
					"text" : "0 0, 1 2, 2 4, 3 5, 4 7, 5 9, 6 11, 7 12"
				}

			}
, 			{
				"box" : 				{
					"editor_rect" : [ 0.0, 28.0, 1440.0, 838.0 ],
					"embed" : 0,
					"id" : "obj-30",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 2,
					"outlettype" : [ "int", "bang" ],
					"patching_rect" : [ 34.833331227302551, 415.33333545923233, 155.0, 22.0 ],
					"saved_object_attributes" : 					{
						"embed" : 0,
						"name" : "",
						"parameter_enable" : 0,
						"parameter_mappable" : 0,
						"range" : 12,
						"showeditor" : 0,
						"size" : 12
					}
,
					"showeditor" : 0,
					"text" : "table"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-28",
					"maxclass" : "number",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 34.833331227302551, 479.33333545923233, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-22",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 40.999997615814209, 14.000000238418579, 100.0, 22.0 ],
					"text" : "udpreceive 7400"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-20",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 176.249984741210938, 169.0, 178.0, 20.0 ],
					"text" : "- - - amplitude from python  - - "
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-16",
					"maxclass" : "ezdac~",
					"numinlets" : 2,
					"numoutlets" : 0,
					"patching_rect" : [ 25.666671395301819, 997.66669225692749, 91.666668057441711, 91.666668057441711 ]
				}

			}
, 			{
				"box" : 				{
					"format" : 6,
					"id" : "obj-11",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 154.249985098838806, 245.333333015441895, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"floatoutput" : 1,
					"id" : "obj-12",
					"maxclass" : "slider",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 154.249985098838806, 196.0, 131.0, 39.0 ],
					"size" : 1.0
				}

			}
, 			{
				"box" : 				{
					"format" : 6,
					"id" : "obj-9",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 357.833315134048462, 245.333333015441895, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"floatoutput" : 1,
					"id" : "obj-7",
					"maxclass" : "slider",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 357.833315134048462, 196.0, 114.0, 38.5 ],
					"size" : 1.0
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-4",
					"maxclass" : "newobj",
					"numinlets" : 6,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 34.833331227302551, 374.83333545923233, 138.0, 22.0 ],
					"text" : "scale 1. 0. 0 7"
				}

			}
, 			{
				"box" : 				{
					"angle" : 270.0,
					"bgcolor" : [ 0.800000071525574, 1.0, 0.400000035762787, 0.460757733840711 ],
					"id" : "obj-69",
					"maxclass" : "panel",
					"mode" : 0,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1460.750034809112549, 658.166678488254547, 295.166671514511108, 430.666675686836243 ],
					"proportion" : 0.5
				}

			}
, 			{
				"box" : 				{
					"angle" : 270.0,
					"bgcolor" : [ 0.400000035762787, 1.0, 0.799999892711639, 0.507055960890008 ],
					"id" : "obj-71",
					"maxclass" : "panel",
					"mode" : 0,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 88.999989628791809, 672.333332717418671, 283.0, 259.333337843418121 ],
					"proportion" : 0.5
				}

			}
, 			{
				"box" : 				{
					"angle" : 270.0,
					"bgcolor" : [ 0.999996185302734, 0.99993908405304, 0.041033305227757, 0.5 ],
					"id" : "obj-73",
					"maxclass" : "panel",
					"mode" : 0,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1096.333347916603088, 44.333333253860474, 409.833348393440247, 184.166674792766571 ],
					"proportion" : 0.5
				}

			}
, 			{
				"box" : 				{
					"angle" : 270.0,
					"bgcolor" : [ 0.988330960273743, 0.400542616844177, 0.99932849407196, 0.502314326973309 ],
					"id" : "obj-81",
					"maxclass" : "panel",
					"mode" : 0,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 26.999969840049744, 6.166657865047455, 784.833353877067566, 268.166675984859467 ],
					"proportion" : 0.5
				}

			}
, 			{
				"box" : 				{
					"angle" : 270.0,
					"bgcolor" : [ 0.990445077419281, 0.502227902412415, 0.032891403883696, 0.514505218227584 ],
					"id" : "obj-74",
					"maxclass" : "panel",
					"mode" : 0,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 29.499997735023499, 311.500000655651093, 514.500010967254639, 337.666669070720673 ],
					"proportion" : 0.5
				}

			}
 ],
		"lines" : [ 			{
				"patchline" : 				{
					"destination" : [ "obj-6", 0 ],
					"source" : [ "obj-10", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-111", 0 ],
					"source" : [ "obj-109", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-33", 1 ],
					"midpoints" : [ 163.749985098838806, 297.0, 784.96845076947011, 297.0 ],
					"source" : [ "obj-11", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-109", 0 ],
					"source" : [ "obj-110", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-1", 0 ],
					"source" : [ "obj-111", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-30", 0 ],
					"source" : [ "obj-113", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-11", 0 ],
					"source" : [ "obj-12", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-33", 0 ],
					"source" : [ "obj-2", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-57", 0 ],
					"source" : [ "obj-22", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-119", 0 ],
					"midpoints" : [ 44.333331227302551, 504.333332896232605, 44.333331227302551, 504.333332896232605 ],
					"order" : 1,
					"source" : [ "obj-28", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-36", 0 ],
					"midpoints" : [ 44.333331227302551, 518.666682124137878, 593.500017404556274, 518.666682124137878 ],
					"order" : 0,
					"source" : [ "obj-28", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-10", 2 ],
					"source" : [ "obj-29", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-60", 0 ],
					"source" : [ "obj-3", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-43", 0 ],
					"source" : [ "obj-30", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-10", 3 ],
					"source" : [ "obj-31", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-10", 1 ],
					"source" : [ "obj-32", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-5", 0 ],
					"source" : [ "obj-33", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-10", 0 ],
					"source" : [ "obj-34", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-33", 0 ],
					"source" : [ "obj-36", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-45", 0 ],
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
					"source" : [ "obj-39", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-30", 0 ],
					"source" : [ "obj-4", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-30", 0 ],
					"source" : [ "obj-40", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-28", 0 ],
					"source" : [ "obj-43", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-48", 1 ],
					"source" : [ "obj-45", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-105", 0 ],
					"midpoints" : [ 61.74998950958252, 969.000003218650818, 420.333333611488342, 969.000003218650818, 420.333333611488342, 898.333337664604187, 444.166671395301819, 898.333337664604187 ],
					"order" : 1,
					"source" : [ "obj-48", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-107", 0 ],
					"midpoints" : [ 61.74998950958252, 969.000003218650818, 420.333333611488342, 969.000003218650818, 420.333333611488342, 889.333337664604187, 771.333327174186707, 889.333337664604187 ],
					"order" : 0,
					"source" : [ "obj-48", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-16", 1 ],
					"order" : 2,
					"source" : [ "obj-48", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-16", 0 ],
					"order" : 3,
					"source" : [ "obj-48", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-16", 1 ],
					"order" : 0,
					"source" : [ "obj-5", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-16", 0 ],
					"order" : 1,
					"source" : [ "obj-5", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-37", 1 ],
					"source" : [ "obj-54", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-39", 0 ],
					"source" : [ "obj-55", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-110", 0 ],
					"source" : [ "obj-57", 3 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-64", 0 ],
					"midpoints" : [ 277.499997615814209, 85.666666626930237, 367.333315134048462, 85.666666626930237 ],
					"source" : [ "obj-57", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-67", 0 ],
					"midpoints" : [ 163.999997615814209, 74.666666746139526, 163.749985098838806, 74.666666746139526 ],
					"source" : [ "obj-57", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-78", 0 ],
					"source" : [ "obj-57", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-2", 0 ],
					"source" : [ "obj-6", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-33", 2 ],
					"source" : [ "obj-6", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-55", 0 ],
					"source" : [ "obj-60", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-65", 0 ],
					"source" : [ "obj-64", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-7", 0 ],
					"source" : [ "obj-65", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-12", 0 ],
					"source" : [ "obj-66", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-66", 0 ],
					"source" : [ "obj-67", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 0 ],
					"source" : [ "obj-7", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-38", 0 ],
					"source" : [ "obj-8", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-4", 0 ],
					"midpoints" : [ 367.333315134048462, 318.666666865348816, 44.333331227302551, 318.666666865348816 ],
					"source" : [ "obj-9", 0 ]
				}

			}
 ],
		"parameters" : 		{
			"obj-33.10::obj-58" : [ "live.gain~[36]", "Osc 3", 0 ],
			"obj-33.10::obj-59" : [ "live.gain~[35]", "Osc 2", 0 ],
			"obj-33.10::obj-60" : [ "live.gain~[34]", "Osc 1", 0 ],
			"obj-33.10::obj-63" : [ "number[35]", "number", 0 ],
			"obj-33.10::obj-69" : [ "number[36]", "number", 0 ],
			"obj-33.10::obj-72" : [ "number[34]", "number[2]", 0 ],
			"obj-33.1::obj-58" : [ "live.gain~[39]", "Osc 3", 0 ],
			"obj-33.1::obj-59" : [ "live.gain~[38]", "Osc 2", 0 ],
			"obj-33.1::obj-60" : [ "live.gain~[37]", "Osc 1", 0 ],
			"obj-33.1::obj-63" : [ "number[37]", "number", 0 ],
			"obj-33.1::obj-69" : [ "number[39]", "number", 0 ],
			"obj-33.1::obj-72" : [ "number[38]", "number[2]", 0 ],
			"obj-33.2::obj-58" : [ "live.gain~[18]", "Osc 3", 0 ],
			"obj-33.2::obj-59" : [ "live.gain~[17]", "Osc 2", 0 ],
			"obj-33.2::obj-60" : [ "live.gain~[16]", "Osc 1", 0 ],
			"obj-33.2::obj-63" : [ "number[11]", "number", 0 ],
			"obj-33.2::obj-69" : [ "number[18]", "number", 0 ],
			"obj-33.2::obj-72" : [ "number[10]", "number[2]", 0 ],
			"obj-33.3::obj-58" : [ "live.gain~[6]", "Osc 3", 0 ],
			"obj-33.3::obj-59" : [ "live.gain~[5]", "Osc 2", 0 ],
			"obj-33.3::obj-60" : [ "live.gain~[4]", "Osc 1", 0 ],
			"obj-33.3::obj-63" : [ "number[12]", "number", 0 ],
			"obj-33.3::obj-69" : [ "number[19]", "number", 0 ],
			"obj-33.3::obj-72" : [ "number[20]", "number[2]", 0 ],
			"obj-33.4::obj-58" : [ "live.gain~[9]", "Osc 3", 0 ],
			"obj-33.4::obj-59" : [ "live.gain~[8]", "Osc 2", 0 ],
			"obj-33.4::obj-60" : [ "live.gain~[7]", "Osc 1", 0 ],
			"obj-33.4::obj-63" : [ "number[6]", "number", 0 ],
			"obj-33.4::obj-69" : [ "number[7]", "number", 0 ],
			"obj-33.4::obj-72" : [ "number[8]", "number[2]", 0 ],
			"obj-33.5::obj-58" : [ "live.gain~[20]", "Osc 3", 0 ],
			"obj-33.5::obj-59" : [ "live.gain~[19]", "Osc 2", 0 ],
			"obj-33.5::obj-60" : [ "live.gain~[21]", "Osc 1", 0 ],
			"obj-33.5::obj-63" : [ "number[13]", "number", 0 ],
			"obj-33.5::obj-69" : [ "number[14]", "number", 0 ],
			"obj-33.5::obj-72" : [ "number[21]", "number[2]", 0 ],
			"obj-33.6::obj-58" : [ "live.gain~[24]", "Osc 3", 0 ],
			"obj-33.6::obj-59" : [ "live.gain~[23]", "Osc 2", 0 ],
			"obj-33.6::obj-60" : [ "live.gain~[22]", "Osc 1", 0 ],
			"obj-33.6::obj-63" : [ "number[24]", "number", 0 ],
			"obj-33.6::obj-69" : [ "number[22]", "number", 0 ],
			"obj-33.6::obj-72" : [ "number[23]", "number[2]", 0 ],
			"obj-33.7::obj-58" : [ "live.gain~[27]", "Osc 3", 0 ],
			"obj-33.7::obj-59" : [ "live.gain~[26]", "Osc 2", 0 ],
			"obj-33.7::obj-60" : [ "live.gain~[25]", "Osc 1", 0 ],
			"obj-33.7::obj-63" : [ "number[25]", "number", 0 ],
			"obj-33.7::obj-69" : [ "number[26]", "number", 0 ],
			"obj-33.7::obj-72" : [ "number[27]", "number[2]", 0 ],
			"obj-33.8::obj-58" : [ "live.gain~[30]", "Osc 3", 0 ],
			"obj-33.8::obj-59" : [ "live.gain~[29]", "Osc 2", 0 ],
			"obj-33.8::obj-60" : [ "live.gain~[28]", "Osc 1", 0 ],
			"obj-33.8::obj-63" : [ "number[28]", "number", 0 ],
			"obj-33.8::obj-69" : [ "number[29]", "number", 0 ],
			"obj-33.8::obj-72" : [ "number[30]", "number[2]", 0 ],
			"obj-33.9::obj-58" : [ "live.gain~[32]", "Osc 3", 0 ],
			"obj-33.9::obj-59" : [ "live.gain~[31]", "Osc 2", 0 ],
			"obj-33.9::obj-60" : [ "live.gain~[33]", "Osc 1", 0 ],
			"obj-33.9::obj-63" : [ "number[31]", "number", 0 ],
			"obj-33.9::obj-69" : [ "number[32]", "number", 0 ],
			"obj-33.9::obj-72" : [ "number[33]", "number[2]", 0 ],
			"obj-5" : [ "live.gain~[3]", "live.gain~", 0 ],
			"parameterbanks" : 			{
				"0" : 				{
					"index" : 0,
					"name" : "",
					"parameters" : [ "-", "-", "-", "-", "-", "-", "-", "-" ]
				}

			}
,
			"parameter_overrides" : 			{
				"obj-33.10::obj-58" : 				{
					"parameter_longname" : "live.gain~[36]"
				}
,
				"obj-33.10::obj-59" : 				{
					"parameter_longname" : "live.gain~[35]"
				}
,
				"obj-33.10::obj-60" : 				{
					"parameter_longname" : "live.gain~[34]"
				}
,
				"obj-33.1::obj-58" : 				{
					"parameter_longname" : "live.gain~[39]"
				}
,
				"obj-33.1::obj-59" : 				{
					"parameter_longname" : "live.gain~[38]"
				}
,
				"obj-33.1::obj-60" : 				{
					"parameter_longname" : "live.gain~[37]"
				}
,
				"obj-33.2::obj-58" : 				{
					"parameter_longname" : "live.gain~[18]"
				}
,
				"obj-33.2::obj-59" : 				{
					"parameter_longname" : "live.gain~[17]"
				}
,
				"obj-33.2::obj-60" : 				{
					"parameter_longname" : "live.gain~[16]"
				}
,
				"obj-33.3::obj-58" : 				{
					"parameter_longname" : "live.gain~[6]"
				}
,
				"obj-33.3::obj-59" : 				{
					"parameter_longname" : "live.gain~[5]"
				}
,
				"obj-33.3::obj-60" : 				{
					"parameter_longname" : "live.gain~[4]"
				}
,
				"obj-33.4::obj-58" : 				{
					"parameter_longname" : "live.gain~[9]"
				}
,
				"obj-33.4::obj-59" : 				{
					"parameter_longname" : "live.gain~[8]"
				}
,
				"obj-33.4::obj-60" : 				{
					"parameter_longname" : "live.gain~[7]"
				}
,
				"obj-33.5::obj-58" : 				{
					"parameter_longname" : "live.gain~[20]"
				}
,
				"obj-33.5::obj-59" : 				{
					"parameter_longname" : "live.gain~[19]"
				}
,
				"obj-33.5::obj-60" : 				{
					"parameter_longname" : "live.gain~[21]"
				}
,
				"obj-33.6::obj-58" : 				{
					"parameter_longname" : "live.gain~[24]"
				}
,
				"obj-33.6::obj-59" : 				{
					"parameter_longname" : "live.gain~[23]"
				}
,
				"obj-33.6::obj-60" : 				{
					"parameter_longname" : "live.gain~[22]"
				}
,
				"obj-33.7::obj-58" : 				{
					"parameter_longname" : "live.gain~[27]"
				}
,
				"obj-33.7::obj-59" : 				{
					"parameter_longname" : "live.gain~[26]"
				}
,
				"obj-33.7::obj-60" : 				{
					"parameter_longname" : "live.gain~[25]"
				}
,
				"obj-33.8::obj-58" : 				{
					"parameter_longname" : "live.gain~[30]"
				}
,
				"obj-33.8::obj-59" : 				{
					"parameter_longname" : "live.gain~[29]"
				}
,
				"obj-33.8::obj-60" : 				{
					"parameter_longname" : "live.gain~[28]"
				}
,
				"obj-33.9::obj-58" : 				{
					"parameter_longname" : "live.gain~[32]"
				}
,
				"obj-33.9::obj-59" : 				{
					"parameter_longname" : "live.gain~[31]"
				}
,
				"obj-33.9::obj-60" : 				{
					"parameter_longname" : "live.gain~[33]"
				}

			}
,
			"inherited_shortname" : 1
		}
,
		"dependency_cache" : [ 			{
				"name" : "adsr-synth.maxpat",
				"bootpath" : "C74:/help/msp",
				"type" : "JSON",
				"implicit" : 1
			}
 ],
		"autosave" : 0,
		"boxgroups" : [ 			{
				"boxes" : [ "obj-71", "obj-3", "obj-60", "obj-55", "obj-39", "obj-104", "obj-54", "obj-37", "obj-45" ]
			}
 ]
	}

}
