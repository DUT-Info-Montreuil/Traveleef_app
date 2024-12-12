import {Component, OnDestroy, OnInit} from '@angular/core';
import * as ol from 'ol';
import { OSM } from 'ol/source';
import { Tile as TileLayer } from 'ol/layer';
import { View } from 'ol';
import { fromLonLat } from 'ol/proj';

@Component({
  selector: 'app-map',
  standalone: true,
  imports: [],
  templateUrl: './map.component.html',
  styleUrl: './map.component.scss'
})
export class MapComponent implements OnInit, OnDestroy {

  private map: ol.Map | undefined;

  ngOnInit(): void {

    if (!this.map) {
      this.map = new ol.Map({
        target: 'map',
        layers: [
          new TileLayer({
            source: new OSM({
              attributions: []
            }),
          }),
        ],
        view: new View({
          center: fromLonLat([2.3522, 48.8566]),
          zoom: 10,
        })
      });
    }
  }

  ngOnDestroy(): void {
    if (this.map) {
      this.map.setTarget(undefined);
      this.map = undefined;
    }
  }

}
